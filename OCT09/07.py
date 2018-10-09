# checking attributes in classes
# Using getattr()
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
print(getattr(emp,'qwerty')) # raises an error because object doesnt contain the specified attribute
# Only objects and attribute name(as string) must be passed as args to getattr()