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

# Step 2: Preprocessing
# Convert 'business_date' to datetime
df['business_date'] = pd.to_datetime(df['business_date'])

# Convert 'metric_value' to numeric, coercing any non-numeric values to NaN
df['metric_value'] = pd.to_numeric(df['metric_value'], errors='coerce')

# Fill NaN values in 'metric_value' column with the mean of the column
df['metric_value'].fillna(df['metric_value'].mean(), inplace=True)

# Sort the data by 'business_date'
df = df.sort_values(by='business_date')

# Step 3: Group the data by month and calculate the average 'metric_value'
# This will aggregate the data monthly if the frequency is monthly
df_grouped = df.groupby(pd.Grouper(key='business_date', freq='M')).agg({'metric_value': 'mean'}).reset_index()

# Step 4: Train-test split (70% train, 30% test)
train_size = int(len(df_grouped) * 0.7)
train, test = df_grouped[:train_size], df_grouped[train_size:]

# Extract the training metric values for time series modeling
train_metric_values = train['metric_value']

# Step 5: Apply Holt-Winters method for Exponential Smoothing
model = ExponentialSmoothing(
    train_metric_values,
    trend='add',  # Additive trend
    seasonal=None,  # No seasonal component
    seasonal_periods=12  # Assuming monthly data, adjust if necessary
)

# Fit the model
hw_model = model.fit()

# Step 6: Forecast for current month and the next month
# We forecast for the test period + the next 2 months
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
