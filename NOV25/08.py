# Count letters using a dictionary
text='The quick brown fox jumped over the lazy dog'
text=text.upper()
counter=dict()
for i in text:
    counter[i]=text.count(i)
print(counter)