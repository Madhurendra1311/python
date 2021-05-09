class Parent:
    def __init__(self,fname,fage):
        self.name = fname
        self.age = fage

    def view(self):
        print(self.name, self.age)

class Child(Parent):
    def __init__(self,fname,fage):
        Parent.__init__(self,fname,fage)
        self.lastname = "madhu"

    def view(self):
        print(self.age, self.lastname, self.name)

Ob = Child(23, 'python')
Ob.view()


# Parent class init method using the child class