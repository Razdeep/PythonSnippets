def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

# Issue here
def factrecursion(n):
    if (n==1 or n==0):
        return 1
    else:
        # return (factrecursion(n-1)+factrecursion(n-2))
        return n*factrecursion(n-1)
# issue ends here

print(factorial(5))
print(factrecursion(5))