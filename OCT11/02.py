# Sophistacted inheritance example

class Parent:
    def setCoordinate(self,x,y):
        self.x=x
        self.y=y

class Child(Parent):
    def draw(self):
        print('Locate point x =',self.x,'on x-axis')
        print('Locate point y =',self.y,'on y-axis')

c=Child()
c.setCoordinate(10,20)
c.draw()