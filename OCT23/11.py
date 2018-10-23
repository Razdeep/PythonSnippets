# arithmetic operations in a single operand

import numpy as np
a=[[0,1],[0,5]]
print(np.sum(a))
print(np.sum(a,axis=0)) # columnwise execution
print(np.sum(a,axis=1)) # row-wise execution