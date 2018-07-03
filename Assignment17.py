# ques1
from tkinter import *
root =Tk()
w=Label(root,text="Hello world")
w.pack()
button=Button(root,text="exit",width=25,fg="red",command=quit)
button.pack()
root.mainloop()


# ques2
from tkinter import *
root =Tk()
def Test():
    print("hello word")
button=Button(root,text="display",width=25,fg="black",command=Test)
button.pack()
root.mainloop()


# ques3
from tkinter import *
root =Tk()
lb=Label(root,text='Edit')
lb.grid(row=0,column=0)
e1=Entry(root,width=10)
e1.grid(row=0,column=1)
frame=Frame(root).grid(row=0)
bframe=Frame(root).grid(row=1)
def Edit():
    res="Welcome to"+el.get()
    lb.configure(text=res)
button1=Button(frame,text="EditText",fg="Blue",command=Edit)
button1.grid(row=0,column=2)
button2=Button(bframe,text="Exit",fg="Green",command=quit)
button2.grid(row=1,column=2)
root.mainloop()


# ques4
from tkinter import *
window=Tk()
window.title("Tkinter")
lb1=Label(window, text="Hello")
lb1.grid(column=0,row=0)
txt=Entry(window,width=10)
txt.grid(column=1,row=0)
def clicked():
    res="you are"+ txt.get()
    lb1.configure(text=res)
btn=Button(window,text="Click me",command=clicked)
btn.grid(column=2,row=0)
window.mainloop()
