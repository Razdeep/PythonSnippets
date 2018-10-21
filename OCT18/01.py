# Figure division
import matplotlib.pyplot as plt
fig=plt.figure()
rect=fig.patch
rect.set_facecolor('green')
x=[0,7,6,12]
y=[3,7,1,12]
x2=[0,4,6,12]
y2=[13,5,8,2]
x3=[20,30,120]
y3=[70,5,100]
fig.add_subplot(3,1,1)
plt.plot(x,y,'r--')
fig.add_subplot(3,1,2)
plt.plot(x2,y2,'y^')
fig.add_subplot(3,1,3)
plt.plot(x3,y3,'b-')
plt.show()