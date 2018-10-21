# Bar graph in matplotlib

import numpy as np
import matplotlib.pyplot as plt

pos=np.arange(6)+0.5
# print(np.arange(6)+.5)
plt.bar(pos,(4,8,12,3,17,6),align='center',color='red')
plt.xlabel('Students')
plt.ylabel('Backlog')
plt.title('LPU Result')
plt.show()