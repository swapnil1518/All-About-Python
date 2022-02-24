# Program to get the 2 largest no from a given array

import numpy as np
a = np.array([12,43,2,100,54,5,68])
# given array first sort then give 2 largest no is descending order

print("The given array is :", a)

# print(np.argsort(a))
# print(np.argsort(a)[-2:])
print(a[np.argsort(a)[-2:][::-1]])

# explanation
# this np.argsort(a)) shows result in ascending order but it shows indexes not the values of the arrays.
# Now according to question to get only 2 highest value no. to get the index of this we are using [-2:]. -2 will show 2 values from last
# [6,3] prints 68,100 but we want print 100, 68 so use [::-1] split function here. this will also print index
# to get the value of the index a[np.argsort(a)[-2:][::-1]] write it in the form of array




