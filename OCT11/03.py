# Multiple inheritance

class A:
    def __init__(self):
        print('In base class')

class B(A):
    def __init__(self):
        print('In B')
class C(A):
    def __init__(self):
        print('In C')

c=C()