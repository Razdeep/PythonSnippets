# median in numpy
import numpy as np 
a = np.array([[30,65,70],[80,95,10],[50,90,60]]) 

print('Our array is:')
print(a)

print('Applying median() function:')
print(np.median(a))

print('Applying median() function along axis 0:')
print(np.median(a, axis = 0))
 
print('Applying median() function along axis 1:')
print(np.median(a, axis = 1))