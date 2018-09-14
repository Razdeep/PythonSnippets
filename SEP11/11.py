# Write the program to replace the text in a file. 
# Your program should prompt the user to enter filename, old string, new string.

fp=open('sample.txt')
fileName=input('Enter filename ')
oldString=input('Enter old string to be replaced ')
newString=input('Enter new string ')
text=fp.readlines()
fp.close()
for i in range(len(text)):
    text[i]=text[i].replace(oldString,newString)
fp=open('sample2.txt','w')
for i in text:
    fp.write(i)
fp.close()