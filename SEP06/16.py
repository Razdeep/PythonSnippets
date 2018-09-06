# creating the file in a different directory

fp=open('custom/file.txt','w')
fp.write("This is another stupid file")
# WARNING: this doesnot create a new directories
fp.close()
fp=open('custom/file.txt')
text=fp.read()
print('Reading from another file located at the custom directory...')
print(text)