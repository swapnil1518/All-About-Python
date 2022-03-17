class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def average(self,a,b):
        s1 = (a+b)/2
        return  s1

s1 = Student(20,40)
print(s1.average(20,40))

class Marks(Student):
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def average(self,a,b):
        s2 = (a+b)/2
        return s2

s2 = Student(50,30)
print(s2.average(50,30))

# gives 2 o/p