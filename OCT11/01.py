# Inheritance

class A:
    def __init__(self):
        print('Hello in base class')

class B(A):
    def __init__(self):
        print('I\'m derived')

b=B()

# NOTE: Constructor of Base class A is not called at first.
#       To call the constructor of the base class, see 04.py