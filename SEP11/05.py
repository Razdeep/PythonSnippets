filename= input('Enter a filename ')
try:
    f=open(filename,'r')
except IOError:
    print('There is no file called',filename)