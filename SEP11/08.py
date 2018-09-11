# Write a program that will count number of characters, words and lines in a file.
fileName='sample.txt'
fp=open(fileName)
text=fp.readlines()
numberOfLines=len(text)
numberOfCharacter,numberOfWords=0,0
for j in range(len(text)):
    for i in range(len(text[j])):
        if text[j][i]==' ' or text[j][i]=='.':
            numberOfWords+=1
        numberOfCharacter+=1
numberOfWords+=1
print('Number of Lines',numberOfLines)
print('Number of Words',numberOfWords)
print('Number of Characters',numberOfCharacter)