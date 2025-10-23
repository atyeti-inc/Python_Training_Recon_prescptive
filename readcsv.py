#read csv and do operation
import pandas as pd

df = pd.read_csv('C:\Timir\Practice Codes\sample_data.csv')


print(df.head())   
print(df.tail()) 

print("checking null values :")

null_row = df.isnull().sum()

print(null_row)

print("Summary\n",df.describe)
