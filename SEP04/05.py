#Find the average of keys of dictionary
dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
sum=0
count=0
for i in dic.keys():
    sum+=i
    count+=1
print('Average is',sum/count)