import pandas as pd

# Assuming your DataFrame is named 'sales_data'
# It should have columns like 'customer_id', 'age', 'purchase_date'

# Filter data for purchases in the past month (adjust based on your date format)
from datetime import date, timedelta

today = date.today()
past_month = today - timedelta(days=30)  # Change 30 to adjust the timeframe

filtered_data = sales_data[(sales_data['purchase_date'] >= past_month) & (sales_data['purchase_date'] <= today)]

# Get the frequency distribution of ages for customers in filtered data
age_counts = filtered_data['age'].value_counts()

# Print the frequency distribution
print(age_counts)
