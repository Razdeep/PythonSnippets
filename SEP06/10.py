# file methods and variables

fp=open('file.txt')
print('Printing file mode:',fp.mode) #default file mode is r
print('Printing file closed status:',fp.closed)
fp.close()
print('Printing file closed status:',fp.closed)