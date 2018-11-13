# column addition 2
# Adding a new column using the existing columns in the dataframe
import pandas as pd
import numpy as np

d={'one':pd.Series([1,2,3],index=['a','b','c']),
    'two':pd.Series([1,2,3,4],index=['a','b','c','d'])
}
df=pd.DataFrame(d)
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
print('Adding a new column using the existing columns in the dataframe')
df['four']=df['one']+df['three']
print(df)