import pandas as pd

# Create a sample dataset
data = {
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerID': ['C001', 'C002', 'C001', 'C003', 'C004'],
    'ProductID': ['P001', 'P002', 'P001', 'P003', 'P002'],
    'Quantity': [2, 1, 3, 5, 2],
    'TotalPrice': [200, 150, 300, 500, 300]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Get a summary of the dataset
print("\nDataFrame Info:")
print(df.info())

# Get basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
mprint(df.isnull().sum())

# Calculate total revenue
total_revenue = df['TotalPrice'].sum()
print(f'\nTotal Revenue: ${total_revenue}')

# Determine the most popular products
popular_products = df.groupby('ProductID')['Quantity'].sum().sort_values(ascending=False)
print('\nMost Popular Products:')
print(popular_products)

# Identify top customers
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False)
print('\nTop Customers:')
print(top_customers)

# Average order quantity
average_quantity = df['Quantity'].mean()
print(f'\nAverage Order Quantity: {average_quantity}')

# Average order price
average_price = df['TotalPrice'].mean()
print(f'Average Order Price: ${average_price}')

