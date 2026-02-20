import pandas as pd
import numpy as np
import matplotlib as plt

file_name='shopping_behavior_updated.csv'
file_pass=f'03 Projects/00 First Project/Data/{file_name}'

df=pd.read_csv(file_pass,sep=',')

# print(df.info())
print(30*'=')
df_age=df['Age']
# میانگین سن ها
print('mean: ',df_age.mean())
print(30*'=')
# از هر سن چندد وجود داره
all_age=df['Age'].value_counts()
print('all age: ')
print(all_age)
print(30*'=')
# بیشترین سنی که وجود داره کدمه
print('max age: ',all_age.idxmax())
print(30*'=')
# کمترین سنی که وجود داره کدمه
print('min age: ',all_age.idxmin())
print(30*'=')