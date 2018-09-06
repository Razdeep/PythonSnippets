# find out sum of all values in a dictionary
a={1:2,2:3,3:4,4:5,5:6}
s1=0 # for calculating sum of keys
s2=0 # for calculating sum of values
for i in a:
    s1+=i
    s2+=a[i]
print('Sum of keys',s1)
print('Sum of values',s2)