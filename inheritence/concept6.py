# Hierarchical Inheritance

class Parent:
    def func1(self):
        print('this is function 1')

class Parent2(Parent):
    def func3(self):
        print('this is function 3')

class Child(Parent):
    def func2(self):
        print('this is function 2')

ob = Child()
ob1 = Parent2()
ob.func1()
ob1.func1()
