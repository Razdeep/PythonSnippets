# wap to check a triangle is equilateral, isosceles or scalene

a=int(input('Enter side a '))
b=int(input('Enter side b '))
c=int(input('Enter side b '))
if a==b==c:
    print('Equilateral triangle')
elif (a==b and a!=c) or (a==c and a!=b) or (b==c and a!=b):
    print('Isosceles triangle')
else:
    print('Scalene triangle')