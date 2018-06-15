#Q1:-
a=(1,2,'akshu',[7,"pin"],{'branch':'cse'})
print('Length of tuple is:',len(a))

#Q2:-
t=(67,84,29,74,66)
print(max(t))
print(min(t))

#Q3:-
b=(8*9*6*11*2)
print(b)

#Q1:-
c=input("enter elements: ")
t1=set()
t1.update(c)
print("elements are:",t1)
d=input("enter elements: ")
t2=set()
t2.update(d)
print("elements are:",t2)
print('Difference between two sets is:',(t1-t2))
print('Difference between two sets is:',(t2-t1))

#Q2:-
print((t1>=t2))
print((t1<=t2))
print((t2>=t1))
print((t2<=t1))


#Q3:-

print('Intersection of two sets is:',t1&t2)

#Q1:-
m=input("enter name: ")
n=input("enter marks: ")
k={'name':m,'marks':n}
print(k)

#Q2:-
t={'prerna':80,'akshi':99,'priya':90,'kaua':66,'dakshi':88}
from collections import OrderedDict
dd=OrderedDict(sorted(t.items(),key=lambda x:x[1]))
print(dd)

#Q3:-Count the number of occurrence of each letter in word "MISSISSIPPI".Store count of every letter with the letter in a dictionary.
l=['M','I','S','S','I','S','S','I','P','P','I']
dict={'M':l.count('M'),'I':l.count('I'),'S':l.count('S'),'P':l.count('P')}
print(dict)

