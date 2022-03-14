class Student:                        # outer class
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()       # object of inner class

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()                 # calling inner class show()

    class laptop:                       # inner class
        def __init__(self):
            self.Brand = 'HP'
            self.CPU = 'i5'
            self.RAM = '1TB'
        def show(self):
            print(self.Brand,self.CPU,self.RAM)

s1 = Student('Swapnil', 2)
s2 = Student('Radhika', 4)

s1.show()
s2.show()

# print(s1.lap.Brand)             # inner class display
# print(s1.lap.CPU)

# lap1 = Student.laptop()
# print(lap1)