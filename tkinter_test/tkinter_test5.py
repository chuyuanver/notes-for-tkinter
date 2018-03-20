from tkinter import *


window = Tk()
'''
change the window size
'''
window.geometry('1024x768')

'''
create a window title
'''
window.title('this is the window title')

'''
create a window icon
'''
window.iconbitmap('F:\\python projects\\images\\testicon1_jdZ_2.ico')

'''
add photo in the window
'''
gif = PhotoImage(file = 'F:\\python projects\\images\\ElasticFarBaboon-max-14mb.gif')
w = Label(window,image = gif)
w.pack()

window.mainloop()


'''
make a slider bar
scale1 = Scale(window, from_ =starting value, to = ending value, orient = HORIZONTAL)
scale1.get() gives the value

'''
