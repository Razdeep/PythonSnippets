# Pickling dump
import pickle
myList=['Hello World','This is Rajdeep','Hope you are doing well...']
fp=open('backup.txt','wb')
pickle.dump(myList,fp)
fp.close()
print('List dumped into backup.txt')