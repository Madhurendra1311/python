# Hybrid Inheritance

class Parent:
    def func1(self):
        print('this is function 1')

class Parent2(Parent):
    def func3(self):
        print('this is function 3')

class Parent3:
    def func4(self):
        print('this is function 4')

class Child(Parent,Parent3):
    def func2(self):
        print('this is function 2')

ob = Child()
ob.func1()
ob.func4()
