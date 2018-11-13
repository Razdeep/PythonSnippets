# column deletion using del operator and pop method of pandas dataframe
import pandas as pd
import numpy as np

d={'one':pd.Series([1,2,3],index=['a','b','c']),
    'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
    'three':pd.Series([10,20,30],index=['a','b','c'])
}
df=pd.DataFrame(d)
print('Before deletion...')
print(df)
del df['one']
print('After column deletion using del operator.')
print(df)
print('Deleting another column with pop method')
df.pop('two')
print(df)