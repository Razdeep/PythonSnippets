# WAP to alias a list
a=[i for i in range(0,11)]
b=a
print('Initial state')
print('a= ',str(a))
print('b= '+str(b),end='\n\n')
print('Deleting the element at index 3 of B...')
del b[3]
print('a= '+str(a))
print('b= '+str(b),end='\n\n')

# Here, on deletion of B, modification is also reflected back
# to the list a. This property is called aliasing
