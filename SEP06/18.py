# reading from pickles
import pickle
fp=open('test.pck','rb')
y=pickle.load(fp)
print(y)
print(type(y))
y=pickle.load(fp)
print(y)
print(type(y))
