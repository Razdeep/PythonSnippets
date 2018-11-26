# Concatenate two dictionaries
mydict={'a':1,'6':2,'c':3}
mydict2={'d':1,'e':2,'f':3}
mydict3=mydict.copy()
mydict3.update(mydict2)
print(mydict)
print(mydict2)
print(mydict3)