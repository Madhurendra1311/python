#Abstraction is one of the most important features of object-oriented programming. It is used to hide the background details or any unnecessary implementation.

from abc import ABC
class type_shape(ABC): 
    def area(self): 
        #abstract method
        pass

class Rectangle(type_shape):
    length = 6
    breadth = 4
    def area(self):
        return self.length * self.breadth

class Circle(type_shape):
    radius = 7
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(type_shape):
    length = 4
    def area(self):
        return self.length*self.length

class triangle:
    length = 5
    width = 4
    def area(self):
        return 0.5 * self.length * self.width


r = Rectangle()                         # object created for the class 'Rectangle'
c = Circle()                            # object created for the class 'Circle'
s = Square()                            # object created for the class 'Square'
t = triangle()                          # object created for the class 'triangle'
print("Area of a rectangle:", r.area())                 # call to 'area' method defined inside the class.
print("Area of a circle:", c.area())                    # call to 'area' method defined inside the class.
print("Area of a square:", s.area())                    # call to 'area' method defined inside the class.
print("Area of a triangle:", t.area())                  # call to 'area' method defined inside the class.
