# concatenate following dictionaries to a new one
# Sample Dictionary
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# Expected result
# {1:10,2:20,3:}


dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4=dict()
for temp in [dic1,dic2,dic3]:
    dic4.update(temp)
print(dic4)