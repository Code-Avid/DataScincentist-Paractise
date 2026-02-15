import pandas as pd

# address of the excel file
fille_name = 'Enhanced_pizza_sell_data_2024-25.xlsx'
file_path = f'Basic/Data/{fille_name}'


xls = pd.ExcelFile(file_path)
print(xls.sheet_names)
df_sheet1 = pd.read_excel(file_path, sheet_name='Sheet1')
print(df_sheet1.head())
print(df_sheet1.columns)
