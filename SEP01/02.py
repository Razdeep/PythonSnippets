# dictionaries method II
# dictionaries dont follow input ordering
eng2sp={'one':'uno','two':'dos','three':'tres'}
print(eng2sp)
# dictionaries are mutable
# changing elements in a dictionary
eng2sp['three']='changed'
# to delete dictionaries
del eng2sp['two']
print(eng2sp)
print(len(eng2sp))
