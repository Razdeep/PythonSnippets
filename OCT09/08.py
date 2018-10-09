# checking attributes in classes
# Using setattr()
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def disp(self):
        print('Name: ',self.name)
        print('Salary',self.salary)

emp=Employee('Sasuke',25000)
emp.disp()

print(getattr(emp,'name')) # returns the value of the member variable
print(setattr(emp,'name','qwerty')) # sets the value of the member variable
print(hasattr(emp,'name')) #Should return True
emp.disp()
# Only objects and attribute name(as string) and value must be passed as args to setattr()