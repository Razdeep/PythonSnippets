# Create a DataFrame from dict of series
import pandas as pd
import numpy as np
d={'one':pd.Series([1,2,3],index=['a','b','c']),
    'two':pd.Series([1,2,3,4],index=['a','b','c','d'])
}
df=pd.DataFrame(d)
print(df)