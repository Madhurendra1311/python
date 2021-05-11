# Private

class Car():
    def __init__(self,windows,doors,enginetype):
        self.__windows = windows
        self.__doors = doors
        self.__enginetype = enginetype

audi = Car(4,4,"Diesel")
print(audi.__windows)