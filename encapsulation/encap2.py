class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.color = color

# encapsulate our code
    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed


ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

#changing ford speed
ford.set_speed(300)

# private
ford.__speed = 400

print(ford.get_speed())
print(ford.color)