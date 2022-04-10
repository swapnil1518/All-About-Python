import array

temp =0
arr = array.array('i',[5, 2, 8, 7, 1, 3, 13, 64, 23, 15, 48, 39, 9])
for i in range(0,len(arr)):
    print(arr[i],end=' ')           # printing original array

#Sort the array in ascending order
for i in range(0,len(arr)):         # 1st element of array
    for j in range(i+1,len(arr)):   # next element of array
        if arr[i]>arr[j]:           # if 1st element is greater than 2nd element
            temp = arr[i]           # store greater no in temp
            arr[i] = arr[j]
            arr[j] = temp
print()
print("sorted elementss : ")
for i in range(0,len(arr)):
    print(arr[i],end=' ')
#print(i(len(arr)-1))