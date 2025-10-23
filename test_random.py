#randon NUMpy

import numpy as np

arr = np.random.randint(1,10, size=(10))
print(arr)

cal_mean = np.mean(arr)
cal_median = np.median(arr)
cal_standard_deviation = np.std(arr)
cal_variance = np.var(arr)

print("Mean :",cal_mean)
print("Median :",cal_median)
print("standard_deviation :",cal_standard_deviation)
print("Variance :",cal_variance)