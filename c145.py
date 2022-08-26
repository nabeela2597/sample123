from tkinter import *

root = Tk()
root.title('Addition')
root.geometry('200x200')
root.configure(bg='pink')

l1 = Label(root,text='Performing Addition',bg='pink',fg='blue')
l1.pack()

def add():
    a = 10
    b = 30
    c = a + b
    print(c)
    l2['text']= c
    
b1 = Button(root, text='Add',command=add, bg='orange')
b1.pack()

l2 = Label(root, bg='pink', fg='blue')
l2.pack()

root.mainloop()