# exploring more properties

import tkinter
root=tkinter.Tk()
w=tkinter.Label(root,text='Red sun',bg='red',fg='white',height=5)
w.pack(fill=tkinter.X)
X=tkinter.Label(root,text='Green Grass',bg='green',fg='white',height=5)
X.pack(fill=tkinter.X)
Y=tkinter.Label(root,text='Red sun',bg='yellow',fg='green',height=5)
Y.pack(fill=tkinter.X)

w=tkinter.Label(root,text='Red sun',bg='red',fg='white',height=5)
w.pack(fill=tkinter.X,pady=10)
X=tkinter.Label(root,text='Green Grass',bg='green',fg='white',height=5)
X.pack(fill=tkinter.X,pady=10)
Y=tkinter.Label(root,text='Red sun',bg='yellow',fg='green',height=5)
Y.pack(fill=tkinter.X,pady=10)

root.mainloop()