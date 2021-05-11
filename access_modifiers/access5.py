## 2) Protected 

# super class
class Student:

     # protected data members
     _name = None
     _roll = None
     _branch = None
     
     # constructor
     def __init__(self, name, roll, branch):  
          self._name = name
          self._roll = roll
          self._branch = branch
     
     # protected member function   
     def _displayRollAndBranch(self):
  
          # accessing protected data members
          print("Roll: ", self._roll)
          print("Branch: ", self._branch)
  
  
# derived class
class Geek(Student):
  
       # constructor 
       def __init__(self, name, roll, branch): 
                Student.__init__(self, name, roll, branch) 
          
       # public member function 
       def displayDetails(self):
                    
                 # accessing protected data members of super class 
                print("Name: ", self._name) 
                    
                 # accessing protected member functions of super class 
                self._displayRollAndBranch()
  
# creating objects of the derived class        
obj = Geek("Madhu", 10525, "ECE") 
  
# calling public member functions of the class
obj.displayDetails() 