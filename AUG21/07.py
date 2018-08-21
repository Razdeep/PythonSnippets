

greeting = 'Hello, world'
print(greeting)
# greeting[0]='G'   # this thing is not allowed
# print(greeting)   # We want to print "Gello, world"

# Instead we use
new_var='G'+greeting[1:]
print(new_var)
