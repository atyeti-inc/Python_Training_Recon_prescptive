import numpy as np


OneD_array=np.arange(10,50)
print(OneD_array)

FourD_array=OneD_array.reshape((4,10))
print(FourD_array)

lit= np.random.randint(1, 100, 20)
print(lit)

print('The mean of the random numbers is',np.mean(lit))
print('The median of the random numbers is', np.median(lit))
print('The deviation of the random numbers is', np.std(lit))
print('The variance of the random numbers is', np.var(lit))

a=np.arange(0,9)
print(a)
A=a.reshape((3,3))
print(A)
b=np.arange(0,9)
print(b)
B=b.reshape((3,3))

C=A+B
print('The Matrix addition is,',C)
D=A*B
print('The matrix multiplication is as follow....', D)
E=A/B
print('The Elemental division is',E)

array1=np.random.randint(1, 1000, 100)
array2=np.sort(array1)[-5:][::-1]
print(array2)

import pandas as pd
Data={'Name':[], 'Department':[], 'Salary':[]}
df=pd.DataFrame(Data)
df_new=pd.DataFrame([{'Name':'Ella', 'Department':'IT', 'Salary':100000},
                     {'Name':'Mike', 'Department':'IT', 'Salary':20000},
                     {'Name':'Harry', 'Department':'IT', 'Salary':150000},
                     {'Name':'Cherry', 'Department':'IT', 'Salary':250000},
                     {'Name':'Tyson', 'Department':'IT', 'Salary':50000}])

df=pd.concat([df,df_new], ignore_index=True)
print(df)
print(df[df['Salary']>50000])


df2 = pd.read_csv(r'C:\Users\HemantGandhi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\sample_data.csv')
print('These are top 5 rows\n', df2.head())
print('These are bottom 5 rows\n', df2.tail())

print('Following are entries with blank values', df2.isnull())

df['New_Salary']=df['Salary'] + df['Salary'] * 0.10
print(df)

print(df2['Trade_Date'])

import matplotlib.pyplot as mp

x=[1,3,5,7]
y=[2,4,6,8]
mp.plot(x,y)
mp.show()

sal=df['New_Salary']
nam=df['Name']

mp.hist(sal)
#mp.hist()
mp.show()


Sly=[100000, 200000, 400000]
Exp=[4,5,6]

mp.scatter(Sly,Exp, marker='o')
mp.xlabel('Salary')
mp.ylabel('Exp')
mp.grid()
mp.show()

import math
number=int(input('Please enter a number for calculations: '))
fact=math.factorial(number)
sqt=math.sqrt(number)
pw=math.pow(number, 2)
print('The factorial of shared number --> ',number,'is ',fact)
print('The Square Root of shared number --> ',number,'is ',sqt)
print('The Power of shared number --> ',number,'is ',pw)


Roll1=[np.random.randint(1,7,1000)]
Roll2=[np.random.randint(1,7,1000)]
Roll=Roll1+Roll2
print(Roll)

mp.hist(Roll)
mp.show()


from datetime import datetime

date='01-Jan-1947'
date2='28-Oct-2025'
Date=datetime.strptime(date, "%d-%b-%Y")
Date2=datetime.strptime(date2, "%d-%b-%Y")
diff= Date2-Date

print('The difference between date1 and date2 is',diff.days)

student_data={
    'Name':['Norman','Thomas'], 'Class':'10th', 'Age':'16'
}

import json
json=json.dumps(student_data)

print(json)
js=r'C:\Users\HemantGandhi\OneDrive - Atyeti Inc\Desktop\jason.txt'
with open(js, 'w+') as file:
    file.write(json)

with open(js, 'r') as file:
    content=file.readlines()
    print(content)

student_data.update({'Age':'18'})

print(student_data)