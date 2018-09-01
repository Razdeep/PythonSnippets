# aliased dictionary
opp={'up':'down','right':'wrong','true':'false'}
# checking aliasing
a1=opp
a1['right']='left'
print(opp)
print(a1)
# they are alias of each other
