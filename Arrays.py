import array

arr = array.array('i',[21,2,3,45,76,87,4,9,5,64])
print(arr)
print(type(arr))
print(arr[6])   #6th element
print(arr[4:8])  #slicing
arr.insert(2,33)   #insert 33 at index 2
print(arr)
arr.pop(4)    # to remove an array, pop, it is done by giving index name
print(arr)
arr.remove(87)  # to remove an element by giving value
print(arr)
arr.reverse()    # to reverse an array
print(arr)