# a program that removes all the occurrences of a specified string from a file
# your program should prompt the user to enter a filename and a string to be removed
print('-------------------------------------------------')
print('This program removes a specific word from a file')
print('-------------------------------------------------')
fileName=input('Enter the filename ')
word=input('Enter the word to be removed from the file ')
fp=open(fileName)
text=fp.readlines()
fp.close()
for i in range(len(text)):
    text[i]=text[i].replace(word,'') # since strings are immutable
print('Text to be saved...')
print(text)
fp=open('sample2.txt','w')
for i in text:
    fp.write(i)
fp.close()
