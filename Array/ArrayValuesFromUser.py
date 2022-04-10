import array

arr = array.array('i',[])
n = int(input("enter the length of Array : "))
for i in range(n):
    x = int(input("enter the value of array : "))
    arr.append(x)
print(arr)