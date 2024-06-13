import matplotlib.pyplot as plt

# Sample data (you can replace this with your actual dataset)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [10000, 12000, 15000, 18000, 20000, 22000, 23000, 21000, 19000, 17000, 15000, 13000]

# Create a line plot
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', color='b', linestyle='-')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 5))
plt.bar(months, sales, color='r')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
