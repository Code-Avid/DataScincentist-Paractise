import pandas as pd

# address of the excel file
fille_name = 'Enhanced_pizza_sell_data_2024-25.xlsx'
file_path = f'Basic/Data/{fille_name}'


xls = pd.ExcelFile(file_path)
# print(xls.sheet_names)
df = pd.read_excel(file_path, sheet_name='Sheet1')


print(df.info())

print(30*'-')
df["Delivery Status"] = df["Delay (min)"].apply(
    lambda x:
    "On Time" if x <= 0
    else "Slight Delay"
    if x <= 10 else "Late"
)
print(df["Delivery Status"].head(15))