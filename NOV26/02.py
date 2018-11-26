# Read and write a csv file using pandas
import pandas as pd
myDataFrame=pd.read_csv('data.csv')
print(myDataFrame.head())

print('Copying data to copy.csv')
myDataFrame.to_csv('copy.csv')