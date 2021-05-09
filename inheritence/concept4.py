# Multiple inheritence

class Parent:
    def func1(self):
        print('this is function 1')

class Parent2:
    def func3(self):
        print('this is function 3')

class Child(Parent,Parent2):
    def func2(self):
        print('this is function 2')

ob = Child()
ob.func1()
ob.func3()
