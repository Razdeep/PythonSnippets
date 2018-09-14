# using entries to add user entered numbers

import tkinter
from tkinter import messagebox
def sum(a,b):
    return a+b
def callback():
    messagebox.showinfo('Result',str(sum(int(entry.get()),int(entry.get()))))
root=tkinter.Tk()
root.geometry('800x600')
label=tkinter.Label(root,text='Enter number #1 ')
entry=tkinter.Entry(root)
label2=tkinter.Label(root,text='Enter number #2 ')
entry2=tkinter.Entry(root)
label.place(x=200,y=100)
label2.place(x=200,y=300)
entry.place(x=300,y=100)
entry2.place(x=300,y=200)
button=tkinter.Button(root,text='Execute',command=callback)
button.place(x=500,y=400)
root.mainloop()