# writing csv file with pandas
import pandas as pd

data=[['Alex',10],['Bob',12],['Clarke',13]]
df=pd.DataFrame(data,columns=['Name','Age'])
print(df)
fileName="newData.csv"
print('Writing data to csv file "'+fileName+'"')
df.to_csv(fileName)