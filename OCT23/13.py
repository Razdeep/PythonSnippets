# using amin and amax methods of numpy

import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.amin(a,axis=0))
print(np.amin(a,axis=1))
print(np.amax(a,axis=0))
print(np.amax(a,axis=1))