# fibonacci series using recursion with range 50
# using dynamic programming
# using dictionaries
# memoization
dic={}
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif dic.get(n):
        return dic.get(n)
    else:
        dic[n]=fibonacci(n-1)+fibonacci(n-2)
        return dic[n]
for i in range(0,100):
    print(fibonacci(i))