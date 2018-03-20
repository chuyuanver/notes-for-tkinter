'''
create click counter
'''

from tkinter import *
window = Tk()

window.geometry('800x600')
window.iconbitmap('F:\\python projects\\images\\testicon1_jdZ_2.ico')

n = 0

button1 = Button(window,text = 'click')
label1 = Label(window,text = 'I count: ')
label2 = Label(window, text = n)

def count_click(event):
    global n
    n+=1
    label2.config(text = n)

button1.bind('<Button-1>',count_click)

button1.grid(row = 0, column = 0, columnspan = 2)
label1.grid(row = 1, column = 0)
label2.grid(row = 1, column = 1)




window.mainloop()
