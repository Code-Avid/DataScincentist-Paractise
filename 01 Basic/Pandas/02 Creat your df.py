import pandas as pd

# address of the excel file
fille_name = 'Enhanced_pizza_sell_data_2024-25.xlsx'
file_path = f'Basic/Data/{fille_name}'


xls = pd.ExcelFile(file_path)
print(xls.sheet_names)
df_sheet1 = pd.read_excel(file_path, sheet_name='Sheet1')
print(df_sheet1.columns)

df1=df_sheet1[['Order ID', 'Restaurant Name', 'Location','Pizza Size', 'Pizza Type','Payment Method']]
print(df1.head())

# df2 = df_sheet1[["Order ID"]].rename(
#     columns={
#         "Order ID": "order_id",
#     }
# )
df3 = df1.copy()
df3["order_id_x10"] = df3["Order ID"] * 10
print(df3.head())
