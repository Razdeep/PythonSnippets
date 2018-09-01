# counting frequency using dictionaries

letterCounts={}
for letter in 'Mississippi':
    letterCounts[letter]=letterCounts.get(letter,0)+1

print(letterCounts)
# we can also access it in a sorted manner
# print(letterCounts.sort())
# Above statement not working
# @TODO