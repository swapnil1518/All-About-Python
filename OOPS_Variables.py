# suppose we have 2 variable of computer class now in Python we can store
# variables inside a special method __init__().
# __init() is used to intialize the variables

class Computer():
    def __init__(self,CPU,RAM):
#print("in init")
        self.CPU = CPU
        self.RAM = RAM
#        print("Confi",CPU,RAM)


    def configuration(self):
        print("Config is", self.CPU,self.RAM)     # here we are using self.CPU because CPU and RAM is a local variable of init method.
        # to use local variable outside the method we are using self.

comp1 = Computer('Ryzen',12)
comp2 = Computer('i5',16)   # this object will call _init__() automatically
# this comp1 and copm2 will not print anything because in __init_ method we are not printing anything

comp1.configuration()
comp2.configuration()
# this comp1 and comp2 will print  because we are calling configuration() method here and inside this method we have print statement

# we are not calling init method anywhere but it is automatically called when an onject is created.
