def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

def factrecursion(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factrecursion(n-1)

print(factorial(5))
print(factrecursion(5))