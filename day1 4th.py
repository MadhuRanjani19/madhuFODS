import pandas as pd
import matplotlib.pyplot as plt

# Sample data (you can replace this with your actual dataset)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [10, 12, 15, 18, 22, 25, 28, 26, 23, 20, 15, 12],  # Example temperature values
    'Rainfall': [50, 40, 30, 20, 10, 5, 5, 10, 15, 20, 30, 40]  # Example rainfall values
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Line plot for temperature
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Temperature'], marker='o', color='b', label='Temperature')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter plot for rainfall
plt.figure(figsize=(10, 5))
plt.scatter(df['Month'], df['Rainfall'], color='r', label='Rainfall')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()






