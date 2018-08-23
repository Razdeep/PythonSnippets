# use of eextend function
list=['a','b','c','d']
list1=['5','6','7']
# list=list+list1 # This also works the same as extend
# list.append(list1) #This doesnot work
list.extend(list1)
print(list)