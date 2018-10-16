# Fetching data from external csv
import matplotlib.pyplot as plt
x=[]
y=[]
fp=open('input.csv','r')
data=fp.read().split('\n')
for i in data:
    val=i.split(',')
    x.append(val[0])
    y.append(val[1])
plt.plot(x,y,'g--')
# plt.plot([1,2,3,4],[5,8,7,25],'g^') # Shows green triangles

plt.title('Rain in december')
plt.xlabel('Days in december')
plt.ylabel('Inches in rain')
plt.show()