# GUI PROGRAMMING
import tkinter

def sum(a,b):
    return a+b

def display():
    print(sum(10,20))

top=tkinter.Tk()
top.geometry('600x400')
b1=tkinter.Button(top,text='Hello',fg='red',command=display)
b1.grid(row=5,column=3)
top.mainloop()