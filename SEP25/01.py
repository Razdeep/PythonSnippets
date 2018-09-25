# Using frames in tkinter

import tkinter
root=tkinter.Tk()
root.geometry('1366x768')
frame=tkinter.Frame(root)
frame.pack()

bottomFrame=tkinter.Frame(root)
bottomFrame.pack(side=tkinter.BOTTOM)

redButton=tkinter.Button(frame,text='Red',fg='red')
redButton.pack(side=tkinter.LEFT)

brownButton=tkinter.Button(frame,text='Brown',fg='brown')
brownButton.pack(side=tkinter.LEFT)

blueButton=tkinter.Button(frame,text='Blue',fg='BLUE')
blueButton.pack(side=tkinter.RIGHT)

blackButton=tkinter.Button(bottomFrame,text='Black',fg='black')
blackButton.pack(side=tkinter.BOTTOM)
root.mainloop()
