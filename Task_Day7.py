# Day 8
# 1. 
import numpy as np
arr=np.arange(10,50)
matrix=arr.reshape(4, 10)
print(matrix)

# 2
import numpy as np
numbers=np.random.rand(20)
mean=np.mean(numbers)
median=np.median(numbers)
SD=np.std(numbers)
variance=np.var(numbers)
print(f"Mean: {mean}, Median: {median}, Standard_deviation: {SD}, Variance: {variance}")

# 3.
import numpy as np
a=np.random.randint(1,10,(3,3))
b=np.random.randint(1,10,(3,3))
Addition=a+b
multiplicaion=a*b 
division=a/b
print("The first matrix:\n", a)
print("The second matric:\n", b)
print("Matric addition is:\n", Addition)
print("Matrix multiplication is:\n",  multiplicaion)
print("Elemenet-wise division is:\n", division)

# 4
import numpy as np
arr=np.random.randint(1,1000, 100)
top5=np.partition(arr, -5)[-5:]
print(top5)

# 5.
import pandas as pd
data={'Name':['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 'Department':['HR', 'IT', 'Finance', 'IT', 'HR'], 'Salary':[50000,60000,70000,20000,45000]}
df=pd.DataFrame(data)
print(df[df['Salary']>50000])

#6.
df=pd.read_csv(r'C:\Users\SumithaaRanganathan\Documents\sample_data.csv')
print("First 5 rows:\n",df.head())
print("Last 5 rows:\n",df.tail())
print("Null Values:\n",df.isnull().sum())
print("Statistics:\n", df.describe())

# 7.
import pandas as pd
df=pd.DataFrame(data)
df['Incremented Salary']=df['Salary']*1.1
avg_dept_salary=df.groupby('Department')['Incremented Salary'].mean()
print(avg_dept_salary)

# 8.
dates=pd.Series(['2020-01-01','2021-02-15','2022-03-30'])
dates=pd.to_datetime(dates)
df=pd.DataFrame({'Date': dates})
df['year']=df['Date'].dt.year
df['Month']=df['Date'].dt.month
print(df)

# 9.
import matplotlib.pyplot as plt
years=[2018,2019,2020,2021,2022]
sales=[100,200,150,180,200]
plt.plot(years,sales)
plt.xlabel('year')
plt.ylabel('Sales')
plt.title('Company Sales Growth')
plt.show()

#10.
import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame(data)
plt.hist(df['Salary'])
plt.xlabel('Salary')
plt.ylabel('frequency')
plt.title('Distribution of Salaries')
plt.grid(True)
plt.show()


# 11.
experience=[1,2,3,4,5]
salary=[30000,35000,40000,45000,50000]
plt.scatter(experience,salary)
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.title('Experience vs Salary')
plt.grid(True)
plt.show()

# 12.
import math
num1=5
num2=4
factorial=math.factorial(num1)
sqrt=math.sqrt(num2)
power=math.pow(num1, num2)
print("Factorial:", factorial, "\nSqrt:", sqrt, "\nPower:",power)

# 13.
import random
import matplotlib.pyplot as plt
import numpy as np

rolls=[random.randint(1,6) + random.randint(1,6) for _ in range(1000)]
plt.hist(rolls, bins=np.arange(2,13,1), edgecolor='black')
plt.xlabel('Sum')
plt.ylabel('frequency')
plt.title('Distribution of dice sums')
plt.show()

# 14.
from datetime import datetime
birthday=datetime(2001,6,18)
today=datetime.now()
days=(today-birthday).days
print(days)

# 15.
import json

student={'name': 'John', 'age':20, 'grade': 'A'}
with open('student.json', 'w') as f:
    json.dump(student, f)
with open('student.json','r') as f:
    data=json.load(f)
data['age']=21
print(data)