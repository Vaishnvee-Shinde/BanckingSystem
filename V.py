import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from datetime import datetime

# Step 1: Connect to the SQLite Database
# Create a connection to the SQLite database
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

# Step 4: Group the data by 'business_date' and calculate the average 'metric_value' per month
# Assuming you want to forecast the metric values aggregated by date
df_grouped = df.groupby(pd.Grouper(key='business_date', freq='M')).agg({'metric_value': 'mean'}).reset_index()

# Step 5: Split the data into training (70%) and testing (30%)
train_size = int(len(df_grouped) * 0.7)
train, test = df_grouped[:train_size], df_grouped[train_size:]

# Extract the training metric values as the target time series
train_metric_values = train['metric_value']

# Step 6: Apply Holt-Winters method for Exponential Smoothing
# Initialize the Holt-Winters model with additive trend and seasonal component
model = ExponentialSmoothing(
    train_metric_values,
    trend='add',  # Using an additive trend
    seasonal=None,  # No seasonal component, adjust if you have seasonality in data
    seasonal_periods=12  # Assuming monthly data, adjust if necessary
)

# Fit the model
hw_model = model.fit()

# Step 7: Forecast for current month and next month
# Forecasting for both the current month and the next one
forecast_periods = len(test) + 2  # One for current and one for next month
forecast = hw_model.forecast(forecast_periods)

# Step 8: Visualize the results
# Plot the training data, test data, and forecasted data
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

# Step 9: Output the forecast for the current and next month
# Get the forecasted values for the current month and the next month
current_month_forecast = forecast[-2]  # Second-to-last forecast for current month
next_month_forecast = forecast[-1]  # Last forecast for next month

print(f"Forecast for the current month: {current_month_forecast}")
print(f"Forecast for the next month: {next_month_forecast}")
