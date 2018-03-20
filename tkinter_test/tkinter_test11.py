'''
use event.
'''

from tkinter import *
window = Tk()
window.geometry('100x100')

canvas1 = Canvas(width = 100,height = 50)

canvas1.pack()
canvas1.create_line(0,0,50,50) #also has color option, (x1,y1,,x2,y2)origins from top left corner

def paint_func(event):
    canvas1.crete[event.x,event.y,event.x+1,event.y+1]
canvas1.bind('B1-Motion',paint_func)
canvas1.pack()
window.mainloop()
