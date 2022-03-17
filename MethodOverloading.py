# Method overloading not possible in python
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def average(self,a,b):
        s1 = (a+b)/2
        return  s1
    def average(self,a,b,c):
        s2 = (a+b+c)/3
        return s2
s1 = Student(30,50)
s2 = Student(80,90,100)
print(s1.average(40,20))
print(s2.averahe(40,60,80))

# gives error

# we can indire tly do overloading by assiging def(self, a= None, b= None)
