'''
bind functions
'''


from tkinter import *
window = Tk()

def haha(event):
    print('clicked')

def jaja(event):
    print('typing')

window.bind('<Key>',jaja)
button1 = Button(window,text = 'click')
'''
<Button-1>: left clicked
'''
button1.bind('<Button-1>',haha)
button1.pack()

window.mainloop()

'''
event:
<Key>: press any key
<Enter>: when cursor moves inside the window
<Leave>: when cursor moves outside the window
<'any_letter'>: when press a certain key on keyboard
<Return>: press enter key
<Double-Button-1>: button1 double clicked
<Shift-Up>: press shift key
<Button-2>: middle click
<Button-3>: right click
etc.
'''
