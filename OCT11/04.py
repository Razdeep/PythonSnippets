class Person:
    def __init__(self,first,last):
        self.firstName=first
        self.lastName=last
    def getName(self):
        return self.firstName+' '+self.lastName

class Employee(Person):
    def __init__(self,first,last,staffnum):
        Person.__init__(self,first,last) 
        # Invoking the constructor of the base class explicitly
        self.staffnum=staffnum
    def toString(self):
        return self.getName()+', '+str(self.staffnum)

emp=Employee('Rajdeep','Roy Chowdhury',99)
print(emp.toString())