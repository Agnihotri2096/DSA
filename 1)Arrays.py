print("**********Array in Python using array module**********")
import array
val = array.array('i', [1,2,3,4,5,6])
print(val)
print("**********")
for i in range(0,6):
    print(val[i],end=",")
print("\n")
print("**********")
for i in val:
    print(i,end=" ")
print("**********")
print(val.typecode) # it shows the type of array
val.reverse()
print(val) # it reverse the array
print("**********")

print("**********Array in Python using numpy module**********")
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr)
from numpy import *
arr1 = array([1,2,3,4,5,6])
print(arr1)
print("using linespace")
arr2 = linspace(0,15,16) # it will create 16 values between 0 to 15
arr3 = arange(1,15,2) # it will create values between 1 to 15 with difference of 2
print(arr2)
print(arr3)
print("using logspace") 
arr4 = logspace(1,40,5) # it will create 5 values between 10^1 to 10^40
print(arr4)