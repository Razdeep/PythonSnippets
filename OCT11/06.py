# Function overriding in case of inheritance

class Parent:
    def display(self):
        print('I\'m the super class')

class Child(Parent):
    def display(self):
        super().display() # Calls the method of the base class
        print('I\'m the child class')

child=Child()
child.display()