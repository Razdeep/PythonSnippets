# using ptp method of numpy
# ptp= (max - min)
import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.ptp(a))
print(np.ptp(a,axis=1))
print(np.ptp(a,axis=0))