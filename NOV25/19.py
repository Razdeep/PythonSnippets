# Appending data in file
fp=open('data.txt','a')
text='This is the new text appended'
fp.write(text)
fp.close()