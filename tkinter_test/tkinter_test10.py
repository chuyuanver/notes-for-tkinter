'''
drawing use canvas
'''
from tkinter import *
window = Tk()
window.geometry('100x100')

canvas1 = Canvas(width = 100,height = 50)

canvas1.pack()
canvas1.create_line(0,0,50,50) #also has color option, (x1,y1,,x2,y2)origins from top left corner

'''
there are other things that can be added into the canvas
create_rectangle creates a rectangle (top left to botton right)
create_oval (centerx,centery,width, height)
create_polygon (x1,y1,x2,y2,x3,y3,...)
optons:
    fill='color'
    outline = 'color'
    width = thickness
'''

window.mainloop()
