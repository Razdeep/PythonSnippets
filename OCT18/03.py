# Bar graph names in matplotlib

import numpy as np
import matplotlib.pyplot as plt

pos=np.arange(6)+0.5
# print(np.arange(6)+.5)
names=['Rajdeep','Utkarsh','Aashu','Kavish','Rohit','Deepak']
plt.bar(pos,(4,8,12,3,17,6),align='center',color='red')
plt.xticks(pos,names)
plt.xlabel('Students')
plt.ylabel('Backlogs')
plt.title('LPU Result')
plt.show()