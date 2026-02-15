import pandas as pd

# address of the excel file
fille_name = 'Enhanced_pizza_sell_data_2024-25.xlsx'
file_path = f'Basic/Data/{fille_name}'


xls = pd.ExcelFile(file_path)
# print(xls.sheet_names)
df = pd.read_excel(file_path, sheet_name='Sheet1')

print(print(df.dtypes))

print(30*'-')
print(df.isna().sum())

print(30*'-')
print(df.dropna())


