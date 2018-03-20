'''
frames
'''
from tkinter import *


window = Tk()
frame1 = Frame(window)
frame2 = Frame(window)

label1 = Label(frame1,text = 'this is in frame1')
button1 = Button(frame1,text = 'f1')


label2 = Label(frame2,text = 'this is in frame2')
button2 = Button(frame2,text = 'f2')

frame1.pack()
frame2.pack(side = BOTTOM)
label1.pack()
label2.pack()
button1.pack()
button2.pack()

window.mainloop()
