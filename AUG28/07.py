# Count the occurrence of element in tuple in a specific range.
def count(a,low,high):
    count=0
    for i in a:
        if(low<=i<high):
            count+=1
    return count
a=(1,2,3,4,5,6,7,8,9)
print(count(a,4,7))