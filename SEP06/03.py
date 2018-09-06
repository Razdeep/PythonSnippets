d1={1:2,2:3,3:4}
d2={5:6,6:7,7:8}
d4=dict(d1)
# d4=d1 # I think these are not same @TODO
d4.update(d2)
print(d4)