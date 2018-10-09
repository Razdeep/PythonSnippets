# Builtin method and variables in classes
# @CAUTION: Not working
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Name',self.name,'  Age',self.age)
emp=Employee('Rajdeep',19)
print('Documentation of the class',emp.__doc__)
print('Name of the class',emp.__name__)
print('in which module class is called',emp.__module__)
print('Bases of the class',emp.__bases__)
print('Dictionary of the class',emp.__dict__)

print()
print(dir(emp))
# @CAUTION: Not working