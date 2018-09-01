# copying in case of dictionaries
opp={'up':'down','right':'wrong','true':'false'}
copy=opp.copy()
copy['right']='left'
print(opp)
print(copy)