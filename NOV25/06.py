# Nested List
a=[i for i in range(11)]
b=[i for i in range(11,21)]
c=[b,a]
print(c)
c.sort()
print(c)
# Sorting is done lexographically, i.e. the contents
# of the nested list are not changed