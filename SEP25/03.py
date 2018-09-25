# anchor component of tkinter
# Use of radio buttons

import tkinter

def sel():
    selection='You selected the option #'+str(var.get())
    label.config(text=selection)

root=tkinter.Tk()
var=tkinter.IntVar()
R1=tkinter.Radiobutton(root,text='Option 1',variable=var,value=1,command=sel)
R1.pack(anchor=tkinter.W)
R2=tkinter.Radiobutton(root,text='Option 2',variable=var,value=2,command=sel)
R2.pack(anchor=tkinter.W)
R3=tkinter.Radiobutton(root,text='Option 3',variable=var,value=3,command=sel)
R3.pack(anchor=tkinter.W)

label=tkinter.Label(root)
label.pack()
root.mainloop()