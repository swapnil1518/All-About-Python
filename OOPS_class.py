# creating class. defining method, creating object and calling method

class Computer():
    def configuration(self):    #self is the object which we are passing
        print("1TB","SSD")

comp1 = Computer()              # creating object of class. comp1 is an object of Compute() class

comp1.configuration()           # calling the method configuration() by using object comp1
Computer.configuration(comp1)   # 2d way of calling a method by using class name. methodname and inside method we can pass comp1 as parameter
# print(type(comp1))

comp2 = Computer()              # creating anothetr object of class. comp2 is an object of Compute() class
comp2.configuration()
Computer.configuration(comp2)