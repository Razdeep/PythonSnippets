# wap to check a string palindrome or not

def reverse(str):
    temp=''
    for i in str:
        temp=i+temp
    return temp

str=input('Enter a string ')
if(str==reverse(str)):
    print('It is palindrome')
else:
    print('Not palindrome')