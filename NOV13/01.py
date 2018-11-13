# Introduction to pandas
# Using pandas series
# Pandas has dataframes and series
# Series is for 1D arrays
import pandas as pd
import numpy as np
data=np.array(['a','b','c','d'])
s=pd.Series(data,index=[100,101,102,103])
print(s)