# Method overriding

class Parent:
    def func1(self):
        print('this is function 1')

class Child(Parent):
    def func1(self):
        print('this is function 2')

Ob = Child()
Ob.func1()