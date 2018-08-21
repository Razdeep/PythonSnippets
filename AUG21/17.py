# wap to check a string palindrome or not using string slicing

text=input('Enter astring to check palindrome ')
if(text==text[::-1]):
    print('Palindrome')
else:
    print('Not palindrome')