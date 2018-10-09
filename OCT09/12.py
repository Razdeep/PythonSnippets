# Destructors
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display(self):
        print('Name',self.__name,'  Age',self.__age)
    def setName(self,name):
        self.__name=name 
    def __del__(self): # The destructor
        print('Hahah, destroying',self.__class__.__name__)


st=Student('Boruto',12)
st.display()
st.setName('Naruto') # Changes the value
st.display()
del st