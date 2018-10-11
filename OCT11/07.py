# Multiple Inheritance

class A:
    def display(self):
        print("i'm the base class")

class B:
    def display(self):
        print("I'm in class B")

class C(A,B): # Inheriting from multiple classes
    def display(self):
        print("I'm the child class")
        super().display()

object=C()
object.display()

# ISSUE in this code