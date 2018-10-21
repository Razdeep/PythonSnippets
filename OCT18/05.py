# Exploring Pie chart

import matplotlib.pyplot as plt
sizes=[50,23,17,5,5]
colors=['yellow','orange','cyan','magenta','red']
plt.pie(sizes,colors=colors,startangle=90)
plt.axis('equal')
plt.show()