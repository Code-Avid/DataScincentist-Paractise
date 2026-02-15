import matplotlib.pyplot as plt
import pandas as pd

# Create a sample DataFrame
# address of the excel file
fille_name = 'customer_bank_data.csv'
file_path = f'Basic/Data/{fille_name}'
df = pd.read_csv(file_path)

### Histogram of Age Distribution===============================================
plt.hist(df['AGE'], bins=10, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.grid(axis='y', alpha=0.5)
plt.show()



