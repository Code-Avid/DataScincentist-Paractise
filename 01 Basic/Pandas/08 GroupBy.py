import pandas as pd

# address of the excel file
fille_name = 'Enhanced_pizza_sell_data_2024-25.xlsx'
file_path = f'Basic/Data/{fille_name}'


xls = pd.ExcelFile(file_path)
# print(xls.sheet_names)
df = pd.read_excel(file_path, sheet_name='Sheet1')


# print(df.info())


print(30*'-')
print(df.groupby("Pizza Size")["Delivery Duration (min)"].mean())


print(30*'-')
print(df.groupby("Payment Method")["Pizza Size"].count())



print(30*'-')

print(df.groupby("Pizza Size")["Delivery Duration (min)"].agg(
    ["mean", "min", "max", "count"]))


print(30*'-')

print(df.groupby(["Pizza Size", "Traffic Level"])["Delivery Duration (min)"].mean())


print(30*'-')

print(df.groupby("Pizza Size")["Delivery Duration (min)"].mean().reset_index())


print(30*'-')
print(df.groupby("Pizza Size")["Delivery Duration (min)"] \
  .mean() \
  .sort_values(ascending=False)
)

print(30*'-')
print(df.groupby("Restaurant Name")["Delay (min)"] \
  .mean() \
  .sort_values(ascending=False) \
  .head(5)
)
