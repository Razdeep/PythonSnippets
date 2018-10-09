# checking attributes in classes
# Using delattr()
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
delattr(emp,'name') # Deletes the entire datatype
print(hasattr(emp,'name')) # Should return False
emp.disp() # This would raise an error
# Only objects and attribute name(as string) must be passed as args to delattr()