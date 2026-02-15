import pandas as pd

# address of the excel file
fille_name = 'Enhanced_pizza_sell_data_2024-25.xlsx'
file_path = f'Basic/Data/{fille_name}'

xls = pd.ExcelFile(file_path)
df_sheet1 = pd.read_excel(file_path, sheet_name='Sheet1')
df1=df_sheet1[['Order ID', 'Restaurant Name', 'Location','Pizza Size', 'Pizza Type','Payment Method','Restaurant Avg Time']]
row = df1.iloc[0]
row_df = df1.iloc[[0]]

# print(row)
# print(30*'-')
# print(row_df)
# rows_list = df1.iloc[:5]
# print(rows_list)

sub_df = df1.iloc[0:5, 0:3]

print(sub_df)

total = df1["Restaurant Avg Time"].sum()
mean_value = df1["Restaurant Avg Time"].mean()

print(total,mean_value)
