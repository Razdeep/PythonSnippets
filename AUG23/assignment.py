def validatePhone(phone):
    if phone>=(10**9) and phone<(10**10):
        return True
    return False

def validateEmail(email):
    broken=email.split('@')
    if(len(broken[0])>5 and len(broken[1])>7 and broken[1].find('.')!=-1):
        return True
    return False

phone=int(input('Enter your phone number '))
email=input('Enter your email address ')
if(validateEmail(email) and validatePhone(phone)):
    print('Phone number and email are correct')
elif not validatePhone(phone):
    print('You have entered wrong phone number')
else:
    print('You have entered wrong email')