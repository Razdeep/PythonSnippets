# pickling
# pickling is used to read as any other object

import pickle
f=open('test.pck','wb')
pickle.dump(12.3,f)
pickle.dump([1,2,3],f)

# writing objects to file
# pickles are used to store tuples,lists, dictionaries