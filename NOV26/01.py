# Create a dataframe having columns Jan,feb,march and populate them
import pandas as pd
myData=[{'jan':10,'feb':20,'march':30},
        {'jan':40,'feb':50,'march':60},
        {'jan':99,'feb':80,'march':90},
        {'jan':90,'feb':70,'march':80},
        {'jan':60,'feb':10,'march':20},
        {'jan':10,'feb':30,'march':50},
        {'jan':40,'feb':90,'march':80}
        ]
myDataFrame=pd.DataFrame(myData)
print(myDataFrame)
print(myDataFrame.iloc[2,1])
print('First 5 rows\n',myDataFrame.head())
print('Last 5 rows\n',myDataFrame.tail())