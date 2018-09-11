# asking  an integer value from the user
# if the user is not an integer then raise a value error

try:
    num=int(input('Enter a number '))
    print('The number is an integer')
except ValueError:
    print('Entered number is not an integer')

# It could be used as default catcher if no exception type is passed