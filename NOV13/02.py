# Working with DataFrame in pandas

import pandas as pd
data=[['Alex',10],['Bob',12],['Clarke',13],['Andrew']]
df=pd.DataFrame(data,columns=['Name','Age'])
# It fills the null values with NaN or None.(eg Andrew)
print(df)