# Classes and objects
# Using constructors with parameters
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def disp(self):
        print('Name: ',self.name)
        print('Salary',self.salary)

emp=Employee('Sasuke',25000)
emp.disp()