# print a pattern A pro mode
result=""
for row in range(0,7):
    for column in range(0,5):
        if((column==0 or column==4) and row!=0) or ((row==0 or row==3) and column>0 and column<4):
            result=result+"*"
        else:
            result=result+" "
    result=result+'\n'
print(result)