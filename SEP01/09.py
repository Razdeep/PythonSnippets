# sparse marix representation using dictioanries
# tuples would be used 
matrix={(0,3):1,(2,1):2,(4,3):3}
print(matrix)

# for fetching the data get method is used
print(matrix.get((0,9),0))
# here the zero in the second argument is returned when the key is not found
print(matrix.get((0,9)))
# By default when keys are absent 'None' is returned