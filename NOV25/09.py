# Iterate python dictionaries using for loop
mydict={'a':1,'6':2,'c':3}
print(mydict)
for i in mydict:
    print(i,mydict.get(i,'Yo! corresponding value not find'))
