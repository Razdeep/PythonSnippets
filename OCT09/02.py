# classes and objects
# Using constructors (Non parameterized)
class Employee:
    def __init__(self):
        self.name='Rajdeep'
        self.salary=20000
    def disp(self):
        print('Name: ',self.name)
        print('Salary',self.salary)

emp=Employee()
emp.disp()