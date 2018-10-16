# Styling graphs
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[5,8,7,25],'r--')
# plt.plot([1,2,3,4],[5,8,7,25],'g^') # Shows green triangles

plt.title('Rain in december')
plt.xlabel('Days in december')
plt.ylabel('Inches in rain')
plt.show()