# Using subplots
import matplotlib.pyplot as plt

fig=plt.figure()

rect=fig.patch
rect.set_facecolor('green')

x=[3,7,8,12]
y=[5,13,2,8]
graph1=fig.add_subplot(1,1,1,facecolor='blue')
graph1.plot(x,y,'red',linewidth=4.0)
plt.show()