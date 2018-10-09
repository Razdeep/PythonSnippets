# checking attributes in classes
# Using hasattr()
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def disp(self):
        print('Name: ',self.name)
        print('Salary',self.salary)

emp=Employee('Sasuke',25000)
emp.disp()

print(hasattr(emp,'qwerty')) # returns False
print(hasattr(emp,'name')) # returns True
print(hasattr(Employee,'name')) # doesnot work directly with classes # returns False
# Only objects and attribute name(as string) must be passed as args to hasattr()