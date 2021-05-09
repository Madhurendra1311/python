class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

# encapsulate our code
    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color


ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

#changing ford speed
ford.set_speed(300)

# private
ford.__speed = 400

print(ford.get_speed())
print(ford.get_color())