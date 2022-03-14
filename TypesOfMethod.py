class Student:
    school = "ABC"                      # class /static variable
    def __init__(self,m1,m2,m3):
        self.m1=m1                      # instance variable
        self.m2=m2
        self.m3=m3

    def avg(self):                      # instance method
        return (self.m1+self.m2+self.m3)/3

    # def get_m1(self):                 # getters/ Accessor (instance variable type 1)
    #     return self.m1
    #
    # def set_m1(self,value):           # setters/ Mutators (instance variable type 2)
    #     self.m1 = 90

    @classmethod                        # class method
    def info(cls):
        return cls.school

    @staticmethod                       # statiuc method
    def defination():
        print("This is static method")

s1 = Student(31,52,87)
s2 = Student(98,56,78)
print(s1.avg())                        # calling instance method
print(s2.avg())
print(Student.info())                  # calling class method
Student.defination()                   # calling static method
