# The process of wrapping up variables and methods into a single entity is known as Encapsulation. It is one of the underlying concepts in object-oriented programming (OOP). It acts as a protective shield that puts restrictions on accessing variables and methods directly, and can prevent accidental or unauthorized modification of data.


class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

#changing ford speed
ford.speed = 250

print(ford.speed)
print(ford.color)