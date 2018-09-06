# script that copies one text file to another

def copyFile(oldFile,newFile):
    fp1=open(oldFile)
    fp2=open(newFile,'w')
    text=fp1.readlines()
    for i in text:
        fp2.write(i)
    fp1.close()
    fp2.close()
    print('File successfully copied')

copyFile('file.txt','copy.txt')