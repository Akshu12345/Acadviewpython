# Ques1
l=[]
for i in range(1,11):
    i=input("enter any value")
    l.append(i)
print(l)


# Ques2
x=5
while(x==5):
    print("Loop is infinite")


# Ques3
l1=[]
l2=[]
for i in range(1,6):
    i=input("enter the values")
    l1.append(i)
print(l1)
for i in range(1,6):
    i=i*i
    l2.append(i)
print(l2)


# Ques4
y=["gorav",15,"akshu",34.3,78,12.7,"bharti",90]
a=[]
b=[]
c=[]
for i in y:
    if isinstance(i,int):
        a.append(i)
print("integer values of a: ",a)
for i in y:
    if isinstance(i,float):
        b.append(i)
print("float values of a:",b)
for i in y:
    if isinstance(i,str):
        c.append(i)
print("string values of a:",c)


# Ques5
u=[]
v=[]
for i in range(1,101):
    if(i%2==0):
        u.append(i)
print("even numbers are: ",u)
for i in range(1,101):
    if(i%2!=0):
        v.append(i)
print("odd numbers are: ",v)


# Ques6
for i in range(0,4):
    for j in range(0,i+1):
        print("*",end="")
    print()


# Ques7
u=input("enter name")
v=input("enter age")
w=input("enter gender")
x=input("ph_no")
a={'name':u,'age':v,'gender':w,'ph_no':x}
for key in a:
    print(key)


# Ques8
l=[]
for i in range(1,10):
    d=input("enter the values")
    l.append(d)
print("list is: ",l)
f=input("enter the value")
if l.index(f):
    g=l.index(f)
    del l[g]
print("new list is: ",l)











