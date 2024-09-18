import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from datetime import datetime

# Step 1: Connect to the SQLite Database
conn = sqlite3.connect('BOE.db')

# Query to fetch the data from the table
query = """
SELECT business_date, unique_identifier_name, dimension_name, dimension_value, dimension_value_id, metric_name, metric_value
FROM BOE_DATA
"""

# Step 2: Load the data into a pandas DataFrame
df = pd.read_sql(query, conn)

# Close the connection to the SQLite database
conn.close()

# Step 3: Preprocessing the data
# Convert 'business_date' to datetime and sort data by date
df['business_date'] = pd.to_datetime(df['business_date'])
df = df.sort_values(by='business_date')

# Step 4: Ensure metric_value is numeric and handle non-numeric values
# Convert metric_value to numeric, invalid parsing will be set as NaN
df['metric_value'] = pd.to_numeric(df['metric_value'], errors='coerce')

# Handle null values: fill NaN values with the mean of the column
df['metric_value'].fillna(df['metric_value'].mean(), inplace=True)

# Step 5: Group the data by 'business_date' and calculate the average 'metric_value' per month
df_grouped = df.groupby(pd.Grouper(key='business_date', freq='M')).agg({'metric_value': 'mean'}).reset_index()

# Step 6: Split the data into training (70%) and testing (30%)
train_size = int(len(df_grouped) * 0.7)
train, test = df_grouped[:train_size], df_grouped[train_size:]

# Extract the training metric values as the target time series
train_metric_values = train['metric_value']

# Step 7: Apply Holt-Winters method for Exponential Smoothing
model = ExponentialSmoothing(
    train_metric_values,
    trend='add',  # Additive trend
    seasonal=None,  # No seasonality
    seasonal_periods=12  # Monthly data assumed
)

# Fit the model
hw_model = model.fit()

# Step 8: Forecast for current month and next month
forecast_periods = len(test) + 2  # Forecast for test period + current month + next month
forecast = hw_model.forecast(forecast_periods)

# Step 9: Visualize the results
plt.figure(figsize=(10, 6))
plt.plot(train['business_date'], train['metric_value'], label='Train Data')
plt.plot(test['business_date'], test['metric_value'], label='Test Data')
plt.plot(df_grouped['business_date'].iloc[train_size:], forecast, label='Forecast')
plt.xlabel('Date')
plt.ylabel('Metric Value')
plt.title('Holt-Winters Forecast of Metric Value')
plt.legend()
plt.grid(True)
plt.show()

# Step 10: Output the forecast for the current and next month in a structured format
current_month_forecast = forecast[-2]  # Second-to-last forecast for current month
next_month_forecast = forecast[-1]  # Last forecast for next month

# Display the forecasted values in a clear format
print("\n--- Forecasted Metric Values ---")
print(f"Forecast for the current month: {current_month_forecast:.2f}")
print(f"Forecast for the next month: {next_month_forecast:.2f}")

# Optional: Display the entire forecasted series
forecast_df = pd.DataFrame({
    'Date': pd.date_range(start=test['business_date'].iloc[0], periods=forecast_periods, freq='M'),
    'Forecasted Metric Value': forecast
})
print("\n--- Full Forecast ---")
print(forecast_df)
