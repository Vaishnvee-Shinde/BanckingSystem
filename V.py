import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from datetime import datetime

# Step 1: Connect to the SQLite Database and fetch data
conn = sqlite3.connect('BOE.db')
query = """
SELECT business_date, unique_identifier_name, dimension_name, dimension_value, dimension_value_id, metric_name, metric_value
FROM BOE_DATA
"""
df = pd.read_sql(query, conn)
conn.close()

# Print the initial shape and content of the DataFrame
print("Initial DataFrame shape:", df.shape)
print("Initial DataFrame preview:\n", df.head())

# Step 2: Preprocessing
# Convert 'business_date' to datetime
df['business_date'] = pd.to_datetime(df['business_date'], errors='coerce')

# Convert 'metric_value' to numeric, coercing any non-numeric values to NaN
df['metric_value'] = pd.to_numeric(df['metric_value'], errors='coerce')

# Print the number of NaN values in the key columns after conversion
print("\nAfter conversion:")
print("NaN values in 'business_date':", df['business_date'].isna().sum())
print("NaN values in 'metric_value':", df['metric_value'].isna().sum())

# Drop rows where 'business_date' or 'metric_value' is NaN
df.dropna(subset=['business_date', 'metric_value'], inplace=True)

# Print the shape after dropping NaN values
print("Shape after dropping NaN values:", df.shape)

# Fill any remaining NaN values in 'metric_value' column with the mean of the column (just to be safe)
df['metric_value'].fillna(df['metric_value'].mean(), inplace=True)

# Sort the data by 'business_date'
df = df.sort_values(by='business_date')

# Print the final state of the data before grouping
print("\nFinal DataFrame shape before grouping:", df.shape)
print("Final DataFrame preview before grouping:\n", df.head())

# Step 3: Group the data by month and calculate the average 'metric_value'
df_grouped = df.groupby(pd.Grouper(key='business_date', freq='M')).agg({'metric_value': 'mean'}).reset_index()

# Print the grouped DataFrame size and preview
print("\nGrouped DataFrame shape:", df_grouped.shape)
print("Grouped DataFrame preview:\n", df_grouped.head())

# Check if the grouped DataFrame is empty after preprocessing
if df_grouped.empty:
    raise ValueError("The DataFrame after grouping is empty. Please check the data preprocessing steps.")

# Step 4: Train-test split (70% train, 30% test)
train_size = int(len(df_grouped) * 0.7)
train, test = df_grouped[:train_size], df_grouped[train_size:]

# Print the sizes of train and test sets
print("\nTrain DataFrame shape:", train.shape)
print("Test DataFrame shape:", test.shape)

# Check if training data is empty
if train.empty:
    raise ValueError("The training data is empty. Please check the data splitting steps.")

# Extract the training metric values for time series modeling
train_metric_values = train['metric_value']

# Print the size and content of the training metric values
print("\nTraining metric values length:", len(train_metric_values))
print("Training metric values preview:\n", train_metric_values.head())

# Check if the train_metric_values is empty or has valid data
if train_metric_values.empty:
    raise ValueError("The training metric values are empty. Please check your data.")

# Ensure the input data to ExponentialSmoothing is a 1D array (Series or NumPy array)
train_metric_values = train_metric_values.values  # Convert to NumPy array if not already

# Step 5: Apply Holt-Winters method for Exponential Smoothing
try:
    model = ExponentialSmoothing(
        train_metric_values,
        trend='add',  # Additive trend
        seasonal=None,  # No seasonal component
        seasonal_periods=None  # Set to None for no seasonality
    )
    
    # Fit the model
    hw_model = model.fit()
    print("\nModel fitting successful!")
except Exception as e:
    print(f"Error during model fitting: {e}")
    raise

# Step 6: Forecast for current month and the next month
forecast_periods = len(test) + 2
forecast = hw_model.forecast(forecast_periods)

# Step 7: Visualize the results
plt.figure(figsize=(10, 6))
plt.plot(train['business_date'], train['metric_value'], label='Train Data')
plt.plot(test['business_date'], test['metric_value'], label='Test Data')
plt.plot(df_grouped['business_date'].iloc[train_size:], forecast[:len(test)], label='Forecasted Test Data')
plt.plot(pd.date_range(start=df_grouped['business_date'].iloc[-1], periods=2, freq='M'),
         forecast[-2:], label='Forecast (Next 2 Months)', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Metric Value')
plt.title('Holt-Winters Forecast of Metric Value')
plt.legend()
plt.grid(True)
plt.show()

# Step 8: Output the forecast for the current and next month in a structured format
current_month_forecast = forecast[-2]  # Second-to-last forecast for current month
next_month_forecast = forecast[-1]  # Last forecast for next month

# Display the forecasted values in a clear format
print("\n--- Forecasted Metric Values ---")
print(f"Forecast for the current month: {current_month_forecast:.2f}")
print(f"Forecast for the next month: {next_month_forecast:.2f}")

# Step 9: Optional: Display the entire forecasted series
forecast_df = pd.DataFrame({
    'Date': pd.date_range(start=test['business_date'].iloc[0], periods=forecast_periods, freq='M'),
    'Forecasted Metric Value': forecast
})
print("\n--- Full Forecast ---")
print(forecast_df)
