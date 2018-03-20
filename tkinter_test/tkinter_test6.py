'''
use grid instead of pack
'''
from tkinter import *

window = Tk()
window.geometry('800x600')
email_label = Label(window,text = 'email address:'.title())
password_label = Label(window,text = 'password:'.title())

email_entry = Entry(window)
password_entry = Entry(window)

'''
grip option: sticky = N/E/S/W
ipadx: inside padding in x direction
pady: outside padding in y direction
columnspan: span a few columns

'''
email_label.grid(row = 0,column = 0,sticky = E,pady = 50)
email_entry.grid(row = 0,column = 1,ipadx = 100)
password_label.grid(row = 1,column = 0,sticky = E,pady = 50)
password_entry.grid(row = 1,column = 1,ipadx = 100)

window.mainloop()
