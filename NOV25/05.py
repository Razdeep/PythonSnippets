# List cloning
a=[i for i in range(0,11)]
b=a[:]
print('Initial state')
print('a= ',str(a))
print('b= '+str(b),end='\n\n')
print('Deleting the element at index 3 of B...')
del b[3]
print('a= '+str(a))
print('b= '+str(b),end='\n\n')

# Here, on deletion of B, modification is not reflected back
# to the list a. This property is called List cloning.