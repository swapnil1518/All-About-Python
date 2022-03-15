# suppose we have class A, a constructor in A. Bow we have another class B in that
# we don't have constructor then object of B will call constructor of A.
# bUt when we have init constructor ib B class also and we want to call A contructor also then we can use SUPER()

class A:
    def __init__(self):
        print("class A constructor")

    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")

class B(A):

    def __init__(self):
        super().__init__()              # this will call class A contructor first then print class B contructor
        print("class B constructor")

    def feature3(self):
        print("feature 3 is working")

# b1 = B()  # this is calling class A constructor when B has no init. when B has init Class B constructor will be called

# now suppose we have once more class C inherting A and B.C(A,B) and when we create obj of c it will call class C conructor and when we
# witing contructor of class C then it will inherti class A. but here it is unfair to avoid this we are using MRO (METHOD RESOLUTION ORDER)
# MRO - whenever we have multiple inheritance. It will go from left to rigt. that is why it is print A class first.

class C(A,B):

    def __init__(self):
        super().__init__()
        print("class C contructor")

c1 = C()