# Pickling load
import pickle
fp=open('backup.txt','rb')
myList=pickle.load(fp)
print(myList)