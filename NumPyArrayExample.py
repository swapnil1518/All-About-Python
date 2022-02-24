# directly we can't use numpy here before that we have to install it in our system. open windows power shell/ cmd and write command.
# pip install numpy
# once it is installed in our sysem then we can use it here and no error will be generated

import numpy as np
# printing 1 D array

a = np.array([1,2,3])
print("Print 1 D array :  ",a)
b = np.array([[1,2,3],[4,5,6]])
print("Printing 2nd array :\n",b)

# printing 5*5 array and print all elements as 0's

c = np.zeros((5,5))     #zeros() is a method used to generate all values as o in an array
print("printing 5*5 array \n", c)

# adding 2 arrays. adding individual elements with each other

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
# np.sum() is used to add 2 arrays. axis=0 is used to add individual elements like 1+4,2+5,3+6
print("Printing sum of 2 arrays: \n", np.sum((a1,a2), axis=0))
# we can also change the value of axis to make the sum in diff ways. like axis =1 means 1+2+3,4+5+6