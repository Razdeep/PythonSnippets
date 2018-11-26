# WAP to write and read files
fp=open('data.txt','r')
text=fp.read() # Reads the entire file at once and returns a single string
print(text)
fp.close()
fp=open('data.txt','r')
text=fp.readline() # Reads a single line and stores as string
print(text)
fp.close()
fp=open('data.txt','r')
text=fp.readlines() # Reads entire file and stores it in a list of strings
print(text)
fp.close()