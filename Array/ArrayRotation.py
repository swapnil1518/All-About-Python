n = int(input("enter no of times : "))
arr = [1,2,3,4,5]
temp =0
for i in range(0,n):
    for j in range(i,n):
        if i<j:
            temp = arr[j+1]
            arr[j+1] = arr[i]
            arr[i] = temp
            print()
        print(arr)
