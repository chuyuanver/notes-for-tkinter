from tkinter  import *

window = Tk()

def name_submit():
    label1.config(text = f'the name is {entry1.get()}')

label1 =Label(window,text ='what is your name')

'''
introduction of entry
'''

entry1 = Entry(window)
button1 = Button(window,text = 'submit',command = name_submit)

entry1.pack()
button1.pack()
label1.pack()

window.mainloop()
