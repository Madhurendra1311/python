## 1) Public

class Geek:
     def __init__(self, name, age):
           self.geekName = name
           self.geekAge = age
  
     def displayAge(self):
            
           # accessing public data member
           print("Age: ", self.geekAge)
  
# creating object of the class
obj = Geek("R2J", 20)
  
# accessing public data member
print("Name: ", obj.geekName)
  
# calling public member function of the class
obj.displayAge()