# single inheritence

class Parent:
    def func1(self):
        print('this is a parent function')

class Child(Parent):
    def func2(self):
        print('this is a child function')

ob = Child()
ob.func1()
