# Function Overloading is not supported in python
# However default arguments can be used instead of that

class Sum:
    # def add(self,a,b):
    #     return int(a)+int(b)
    def add(self,a,b,c=0):
        return int(a)+int(b)+int(c)
sum=Sum()
print(sum.add(2,3))