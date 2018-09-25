# Tweaking appearances of Tkinter components
# using relief: FLAT, RAISED, SUNKEN, GROOVE
import tkinter
root=tkinter.Tk()
B1=tkinter.Button(root,text='FLAT',relief=tkinter.FLAT)
B2=tkinter.Button(root,text='RAISED',relief=tkinter.RAISED)
B3=tkinter.Button(root,text='SUNKEN',relief=tkinter.SUNKEN)
B4=tkinter.Button(root,text='GROOVE',relief=tkinter.GROOVE)
B1.pack()
B2.pack()
B3.pack()
B4.pack()
root.mainloop()