#Adding a new column by passing as Series
import pandas as pd 
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])} 
df = pd.DataFrame(d) 
print ("Adding a new column by passing as Series:") 
df['three']=pd.Series([10,20,30],index=['a','b','c']) 
print(df)
#Adding a new column using the existing columns in DataFrame
print("Adding a new column using the existing columns in DataFrame:") 
df['four']=df['one']+df['three'] 
print (df)