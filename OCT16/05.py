# More Styling in the graph
import matplotlib.pyplot as plt

fig=plt.figure()
rect=fig.patch
rect.set_facecolor('green')
x=[3,7,8,12]
y=[5,13,2,8]
graph1=fig.add_subplot(1,1,1)
graph1.plot(x,y,'red',linewidth=4.0)

graph1.tick_params(axis='x',color='blue')
graph1.tick_params(axis='y',color='white')

graph1.spines['top'].set_color('w')
graph1.spines['left'].set_color('w')
graph1.spines['right'].set_color('w')
graph1.spines['bottom'].set_color('w')

graph1.set_title('Random graph',color='blue')
graph1.set_xlabel('This is the x-axis',color='yellow')
graph1.set_ylabel('This is the y-axis',color='yellow')

plt.show()