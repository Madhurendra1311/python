# All the class variable are public

class Car():
    def __init__(self,windows,doors,enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype

audi = Car(4,5,"Diesel")
print(audi.windows)