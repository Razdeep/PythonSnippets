# reverse a string using function

a="The quick brown fox jumped over the lazy dog"
def reverse(a):
    temp=''
    for i in range(0,len(a)):
        temp=a[i]+temp
    return temp

print(reverse(a))