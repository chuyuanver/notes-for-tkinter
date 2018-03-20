'''
make menu
'''
from tkinter import *
window = Tk()

my_menu = Menu(window)
window.config(menu = my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='open') # add the menu items, can add commands to it
file_menu.add_separator() # add a seperator
file_menu.add_command(label='help')



edit_menu = Menu(my_menu)
my_menu.add_cascade(label = 'edit', menu = edit_menu)


window.mainloop()
