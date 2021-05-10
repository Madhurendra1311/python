# All the class variable are protected

class Car():
    def __init__(self,windows,doors,enginetype):
        self._windows = windows
        self._doors = doors
        self._enginetype = enginetype

class Truck(Car):
    def __init__(self,windows,doors,enginetype,horsepower):
        super().__init__(windows,doors,enginetype)
        self.horsepower = horsepower
       

truck = Truck(4,4,"Diesel",4000)
truck._doors = 5
print(truck._windows)