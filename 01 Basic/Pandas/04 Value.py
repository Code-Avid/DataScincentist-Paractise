import pandas as pd

# address of the excel file
fille_name = 'Enhanced_pizza_sell_data_2024-25.xlsx'
file_path = f'Basic/Data/{fille_name}'

xls = pd.ExcelFile(file_path)
df_sheet1 = pd.read_excel(file_path, sheet_name='Sheet1')
df1=df_sheet1[['Order ID', 'Restaurant Name', 'Location','Pizza Size', 'Pizza Type','Payment Method','Restaurant Avg Time']]

count_n = (df1["Pizza Size"] == "Large").sum()
print(count_n)
print(30*'=')

counts = df1["Pizza Size"].value_counts()
print(counts)
print(30*'=')
counts_df = df1["Pizza Size"].value_counts().reset_index()
print(counts_df)
print(30*'=')
most_common = df1["Pizza Size"].value_counts().idxmax()
most_common_count = df1["Pizza Size"].value_counts().max()
print(most_common,most_common_count)
print(30*'=')
least_c = df1["Pizza Size"].value_counts().idxmin()
least_c_count = df1["Pizza Size"].value_counts().min()
print(least_c,least_c_count)