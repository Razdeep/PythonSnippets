# write a program to print the sum of all even numbers from 100 to 200 using recursion
def recur(last):
    if last==200:
        return 200
    if last%2==1:
        last+=1
    return last+recur(last+2)

print(recur(100))