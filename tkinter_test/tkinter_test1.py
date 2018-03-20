from tkinter import *
'''
create window
'''
window = Tk()


'''
add label
'''
test_label = Label(window,text = 'hello world!')
label_2 = Label(window,text = 'hello world! again')


'''
add a button
padx,pady: increase the horizontal and vertial size of the button
fg: color of the text
bg: color of the button
'''
test_button = Button(window,text = 'Hit',padx = 10,pady = 10,fg = 'blue',bg = 'red')


'''
pack the stuff in the window
'''
test_label.pack()
label_2.pack()
test_button.pack(side = LEFT)


'''
make into a loop
'''
window.mainloop()
