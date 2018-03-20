from tkinter import *
window = Tk()

'''
config the widget in the window
'''
def button_func():
    button1.config(text = 'howdy')

'''
use the command to make a call back function
'''


button1 = Button(window,text = 'haha',command = button_func)
button1.pack()

window.mainloop()
