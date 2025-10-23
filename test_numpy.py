#NUMpy

#Numpy array form 1-50

import numpy as np
print("\nNumpy array form 10-50")
arr = np.arange(10, 50)
print(arr.reshape(4,10))

#Random numpy 1-10 and do mean,median,standard deviation,variance
print("\nRandom numpy 1-10 and do mean,median,standard deviation,variance")
arr1 = np.random.randint(1,10, size=(10))
print(arr1)

cal_mean = np.mean(arr1)
cal_median = np.median(arr1)
cal_standard_deviation = np.std(arr1)
cal_variance = np.var(arr1)

print("Mean :",cal_mean)
print("Median :",cal_median)
print("standard_deviation :",cal_standard_deviation)
print("Variance :",cal_variance)

#3*3 matrix a and b and perform addition ,multiplication and division
print("\n3*3 matrix a and b and perform addition ,multiplication and division")
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

add = a+b
mul = a*b
div = a/b

print("Matrix a :\n",a)
print("Matrix b :\n",b)
print("Matrix Sum :\n",add)
print("Matrix Multiplication :\n",mul)
print("Matrix Division :\n",div)

print("\n1D array of random 1-1000 numbers and with top five largest val")
arr1d = np.random.randint(1,100,size=(100))
print(arr1d)
top_val = np.sort(arr1d)[-5:]
print("5 largest val of array are ", top_val)