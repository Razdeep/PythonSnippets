# spinbox component of tkinter
import tkinter

root = tkinter.Tk()

w = tkinter.Spinbox(root, from_=0, to=100,width=10)
w.pack()
x = tkinter.Spinbox(root, values=('Easy','Medium','Hard'),width=10)
x.pack()
y = tkinter.Spinbox(root, values=(3,7,97),width=10)
y.pack()

# Setting u default values
var=tkinter.IntVar()
var.set(69)
z = tkinter.Spinbox(root, from_=0, to=100,width=10,textvariable=var)
z.pack()

root.mainloop()