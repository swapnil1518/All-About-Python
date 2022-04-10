#creating a 2d array (3 rows by 7 columns) and populating it with numbers
matrix=[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21]
rows=len(matrix) #finding the max number of rows in the matrix, in this case 3
columns=len(matrix[0]) #finding the max number of columns in each row, 7 in this case
print(matrix)
number=int(input("What number are you looking for?"))
for i in range(rows):
      for j in range(columns):
        if matrix[i][j]==number:
          print("Found it!")
          break
else:
  print("not found")