# Classes and objects
# using static variable(count) in classes
class Employee:
    # This variable is a static variable
    count=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.count+=1
    def disp(self):
        print('Name: ',self.name)
        print('Salary',self.salary)
    def getCount(self):
        print('Total Number of employees are',Employee.count)

emp1=Employee('Sasuke',25000)
emp1.disp()
emp2=Employee('Naruto',30000)
emp2.disp()
emp3=Employee('Sakura',10000)
emp3.disp()
emp1.getCount()