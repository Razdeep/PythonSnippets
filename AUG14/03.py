#wap to find the numbers which are divisible by 3
a=int(input('Enter starting range '))
b=int(input('Enter ending range '))
number=int(input('Enter the number whose multiples you want to find in the range '))
print('Numbers which are divisible')
for i in range(a,b+1):
    if i%number==0:
        print(i,end=' ')