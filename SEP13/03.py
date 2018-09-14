# tkinter message box

import tkinter
from tkinter import messagebox
def callback():
    messagebox.showinfo('Hello Tkinter','This is some random text')

root=tkinter.Tk()
root.geometry('640x480')
button=tkinter.Button(root,text='Generate MessageBox',command=callback,width=20,height=3,activebackground='green',fg='blue',bg='white')
button.pack()
root.mainloop()