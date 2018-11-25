# wap to print the pattern A
for i in range(0,7):
    for j in range(0,5):
        if(i==0):
            if(j>0 and j<4):
                print('*',end='')
            else:
                print(' ',end='')
        elif(i==3):
            print('*',end='')
        else:
            if(j==0 or j==4):
                print('*',end='')
            else:
                print(' ',end='')
    print()    
