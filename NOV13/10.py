# reading csv file with pandas
import pandas as pd
df=pd.read_csv('data.csv')
# df=pd.read_csv('data.csv',header=None) # Use this to ignore header from the csv
print(df)