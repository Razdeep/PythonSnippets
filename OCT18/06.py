# Pie chart legends
import matplotlib.pyplot as plt
sizes=[4,8,12,3,17]
labels=['windows','apple','android','blackberry','linux']
colors=['yellow','orange','cyan','magenta','red']
plt.pie(sizes,labels=labels)
plt.legend(loc='lower right')
# plt.legend(loc='best')
plt.axis('equal')
plt.show()