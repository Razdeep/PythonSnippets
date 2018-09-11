# Write a program that write 100 random integers. 
# Integers are separated by space in file. 
# Read the data back from the file and display the sorted data.
import random
fileName='random.txt'
fp=open(fileName,'w')
text=''
for i in range(100):
    text+=str(random.randint(0,100))
    text+=' '
fp.write(text)
fp.close()

fp=open(fileName)
text=fp.readline()
text=text.split(' ')
text=[int(i) for i in text]
for i in text:
    print(i)