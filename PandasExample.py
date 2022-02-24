import pandas as pd

# Converting a list into dataframe
l1 = [10,20,30,40,50]
print("The List is : \n", l1)
data1 = pd.DataFrame(l1)
print("Convterted list into dataframe : \n",data1)

# Converting a dictionary into dataframe

dt1 = {'Fruit_Name':['Apple','Mango','Guava','Banana'],'Count':[12,24,36,48]}
# created a dictionary with key fruitname and has 4 respective values simalarly another key count and respective vales
print("The Dictinary is :\n", dt1)
data2 = pd.DataFrame(dt1)
print("Converted Dictionary into dataframe :\n",data2)

