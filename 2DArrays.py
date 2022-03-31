import array

#arr = array.array('i',[[1,2,3,4,5,6],[34,56,67,89,32],[9,8,7,6,5]])
ar = [[1,2,3,4,5,6],[34,56,67,89,32],[9,8,7,6,5]]

print(ar)
for i in ar:                  # print all arrays
    for j in i:
        print(j,end=" ")
    print()    # this will print in next line
print(ar[2][3])   # accessing a particular element.  from 2nd array print 3rd index element

# to insert a new array
ar.insert(1,[4,2,6,8])
print(ar)

