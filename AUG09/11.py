# PASSWORD CHECKING WITH A WHILE LOOP
i=0
while(True):
    password=input('Enter password ')
    if(i>=2):
        print('Access denied')
        break
    i=i+1
    if(password=="password"):
        print('Login successful')
        break
    print('Try again')
