# min and max functions on dictionaries
d={321:10,322:56,323:7}
print(min(d,key=d.get)) # returns the key where the value is min
print(max(d,key=d.get)) # returns the key where the value is max