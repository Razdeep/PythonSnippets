# Menu button in tkinter
import tkinter

root=tkinter.Tk()
mb=tkinter.Menubutton(root,text='File')
mb.menu=tkinter.Menu(mb,tearoff=0)
mb['menu']=mb.menu

mayoVar=tkinter.IntVar()
ketchVar=tkinter.IntVar()


mb.menu.add_checkbutton(label='asdas',variable=mayoVar)
mb.menu.add_checkbutton(label='ajdnajd',variable=ketchVar)
mb.place(x=0,y=0)
root.mainloop()