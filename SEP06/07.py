# writing contents to file
fp=open('file.txt','w')
text=input('Enter some text to save in file.txt\n')
fp.write(text)
fp.close()