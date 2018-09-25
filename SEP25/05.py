# Using checkbutton/checkboxes in tkinter
import tkinter
root=tkinter.Tk()
checkVar1=tkinter.IntVar()
checkVar2=tkinter.IntVar()
C1=tkinter.Checkbutton(root,text='Music',variable=checkVar1,onvalue=1,offvalue=0,height=0,width=0)
C2=tkinter.Checkbutton(root,text='Videos',variable=checkVar2,onvalue=1,offvalue=0,height=0,width=0)
C1.pack()
C2.pack()
root.mainloop()