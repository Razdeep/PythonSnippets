# WAP to traverse a string using for loop and while loop
text='Hello World'
for i in text:
    print(i,end='')
print()
i=0
while(i<len(text)):
    print(text[i],end='')
    i+=1
print()