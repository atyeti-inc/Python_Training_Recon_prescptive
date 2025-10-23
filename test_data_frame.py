#pandas examples

import pandas as pd

df = pd.DataFrame([
    {'Name': 'Ramesh', 'Department': 'IT', 'Age': 35, 'Salary': 50000},
    {'Name': 'Suresh', 'Department': 'Finance', 'Age': 36,'Salary': 45000},
    {'Name': 'Mahesh', 'Department': 'HR', 'Age': 30,'Salary': 30000}
])	


print(df,"\n")

#adding new data to data frame
new_data = pd.DataFrame([
    {'Name': 'Ganesh', 'Department': 'Finance', 'Age': 29, 'Salary': 42000},
    {'Name': 'Amit', 'Department': 'IT', 'Age': 34,'Salary': 55000},
    {'Name': 'Sumit', 'Department': 'HR', 'Age': 28,'Salary': 28000}
])

df=pd.concat([df,new_data],ignore_index=True)

print("Added new rows :\n",df)

# Filter rows where Salary is greater than or equal to 50000
print("Salary greater equals to 50k :\n",df[df['Salary'] >= 50000])

# Add a column with 10% increment in salary
print("\nIncrement added 10% :\n")
df['Increment 10'] = df['Salary']*1.10

print(df)

# Group by Department and show average incremented salary per department
grouped = df.groupby('Department')['Increment 10'].mean()

print("\nAverage incremented salary per department:\n", grouped)

df.to_csv('C:\Timir\Practice Codes\DataFrame_data.csv', index=False)