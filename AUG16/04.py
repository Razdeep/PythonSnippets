# printing B pattern

result=''
for i in range(0,7):
    for j in range(0,5):
        if(j==0 or ((i==0 or i==6 or i==3) and j<4) or (j==4 and i!=0 and i!=3 and i!=6)):
            result=result+'B'
        else:
            result=result+' '
    result=result+'\n'
print(result)