# fibonacci series pro mode
a=0
b=1
n=int(input('Entre the number which u want to find the fibonacci numbers '))
i=0
while i<n:
    print(a+b)
    a,b=b,a+b