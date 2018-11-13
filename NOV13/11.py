# tweaking datatypes of pandas dataFrame
# BUG HERE

import pandas as pd
import numpy as np
df=pd.read_csv('data.csv',dtype={'salary':np.float64})
print(df.dtypes)