# Another way to access private members
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display(self):
        print('Name',self.__name,'  Age',self.__age)
    def setName(self,name):
        self._Student__name=name #self. _ ClassName _ _ attributeName

st=Student('Boruto',12)
st.display()
st.__name='Naruto' # Doesn't change the value
st.display()
st.setName('Naruto') # Changes the value
st.display()