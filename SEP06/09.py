# reading and writing in file in same script

fp=open('file.txt','w')
text=input('Enter some text to put in the file.txt\n')
fp.write(text)
text=''
fp.close()

fp=open('file.txt') # reassigning file pointer
text=fp.read()
print('Reading file...')
print(text)
fp.close()