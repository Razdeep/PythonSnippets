# using listboxes in tkinter

import tkinter
root=tkinter.Tk()

lb1=tkinter.Listbox(root)
lb1.insert(1,'Python')
lb1.insert(2,'Perl')
lb1.insert(3,'C')
lb1.insert(4,'php')
lb1.insert(5,'C++')

lb1.pack()
root.mainloop()