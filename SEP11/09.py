# Suppose that a text file contains an unspecified number of scores.
# Write a program that reads the scores from the file and display their total and average.
# Scores are separated by blanks.
# Your program should prompt the user to enter a filename.

fileName=input('Enter the file name (Default : scores.txt) ')
if(fileName==''):
    fileName='scores.txt'
fp=open(fileName)
scores=fp.readline()
scores=scores.split(' ')
print(scores)
sum=0
for i in scores:
    sum+=int(i)
print('Total sum is',sum)
print('Average of the scores is',sum/len(scores))