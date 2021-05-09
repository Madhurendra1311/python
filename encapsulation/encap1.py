class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

#changing ford speed
ford.speed = 200

print(ford.speed)
print(ford.color)