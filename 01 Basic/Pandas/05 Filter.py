import pandas as pd

# address of the excel file
fille_name = 'Enhanced_pizza_sell_data_2024-25.xlsx'
file_path = f'Basic/Data/{fille_name}'

xls = pd.ExcelFile(file_path)
df1 = pd.read_excel(file_path, sheet_name='Sheet1')

print(df1.columns)

print(df1[df1["Order Hour"] > 10])
print(30*'=')
print(df1[(df1["Order Hour"] > 10) & (df1["Pizza Size"] == "Large")])

print(30*'=')
print(df1[(df1["Pizza Size"] == "Large") | (df1["Pizza Size"] == "Medium")])

print(30*'=')
print(df1[df1["Pizza Size"].isin(["Large", "Medium"])])


print(30*'=')
print('not nal')
print(df1[df1["Order Hour"].notna()])

print(30*'=')
print('is nal')
print(df1[df1["Order Hour"].isna()])


print(30*'=')
print(df1[df1["Order ID"].str.contains("ORD001")])

print(30*'=')
df1["Order Date"] = pd.to_datetime(df1["Order Date"])
print(df1[df1["Order Date"] > "2024-01-01"])


