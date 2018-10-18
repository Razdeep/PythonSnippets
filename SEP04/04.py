# max function in dictionary
dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
max=-299
for i in dic.values():
    if i>max:
        max=i
print(max)