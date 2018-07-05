# Ques1
from tkinter import *
root=Tk()
dict={"Äkshita Sharma":354,"Gourav Sareen":361,"varinda":353,"Bharti":352,"Partap":355,"Parul":364,"Dakshina":398,"Ruby":366,"Diksha":411,"Priyanka":413}
x=StringVar()
l3=Label(root,text=" ")
l3.grid(row=1,column=1)
def display(evt):
    l3.config(text=dict[l1.get(ACTIVE)])
    print(dict[l1.get(ACTIVE)])
L1=Label(root,text="Name:")
L1.grid(row=0,column=0)
L2=Label(root,text="Mobile_no:")
L2.grid(row=0,column=1)
s1=Scrollbar(root,orient=VERTICAL)
l1=Listbox(root,height=10,yscrollcommand=s1.set)
for i in dict.keys():
    l1.insert(END,i)
s1.config(command=l1.yview)
l1.grid(row=1,column=0,rowspan=3)
s1.grid(row=1,column=0,rowspan=3,sticky=E+N+S)
l1.bind("<<ListboxSelect>>",display)
root.mainloop()


# Ques2
from tkinter import *
root=Tk()
dict1={"Äkshita Sharma":354,"Gourav Sareen":361,"varinda":353,"Bharti":352,"Partap":355,"Parul":364,"Dakshina":398,"Ruby":366,"Diksha":411,"Priyanka":413}
x=StringVar()
y=StringVar()
L3=Label(root,text="")
L3.grid(row=1,column=1)
def show1(evt):
    L3.config(text=dict1[l1.get(l1.curselection())])
def show2():
    dict1[x.get()]=y.get()
    z=x.get()
    print(dict1)
    l1.insert(END,z)
    print(z)
    show3()
L1=Label(root,text="Name:").grid(row=0,column=0)
L2=Label(root,text="Roll_no:").grid(row=0,column=1)
s1=Scrollbar(root,orient=VERTICAL)
l1=Listbox(root,height=10,yscrollcommand=s1.set,exportselection=0)
def show3():
    s1.config(command=l1.yview)
    l1.grid(row=1,column=0,rowspan=3)
    s1.grid(row=1,column=0,rowspan=3,sticky=E+N)
    l1.bind("<<ListboxSelect>>",show1)
for i in dict1.keys():
    l1.insert(END,i)
    print(i)
    show3()
l4=Label(root,text="enter name=").grid(row=4,column=0)
L5=Label(root,text="enter roll_no=").grid(row=4,column=1)
e1=Entry(root,textvariable=x).grid(row=5,column=0)
e2=Entry(root,textvariable=y).grid(row=5,column=1)
b1=Button(root,text="Go",command=show2).grid(row=6)
root.mainloop()
