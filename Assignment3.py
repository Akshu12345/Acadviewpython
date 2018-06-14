#Q1:-Create a list with user defined inputs.

a=input("enter elements: ")
l=[]
l.append(a)
print("elements are: ",l)


#Q2:-Add the following list to above created list:
    #'google','apple','facebook','microsoft','tesla'

m=['google','apple','facebook','microsoft','tesla']
print(l+m)


#Q3:-Count the no. of times an object occur in the list.

g=['goru','akshu','bharti','akshu','varinda']
print(g.count('akshu'))


#Q4:-Create a list with numbers and sort it in ascending order.

a=[59,45,10,99,104]
a.sort()
print('Sorted elements are: ',(a))


#Q5:-Given are two one-dimensional arrays A and B which are sorted in ascending order.Write a program to merge them into a singal sorted array C that contains every item from arrays A and B,in ascending order.[List]

A=[12,34,54,10,8]
B=[70,61,85,90,88]
A.sort()
B.sort()
C=print('Sorted elements are: ',(A+B))


#Q6:-Implement a stack and queue using lists.

#STACK
stack=[3,5,7,9]
stack.append(10)
stack.append(20)
print(stack)
stack.pop()
print(stack)

#QUEUE
from collections import deque
queue=deque([14,16,18,20])
print(queue)
queue.append(22)
queue.append(24)
print(queue)
queue.popleft()
print(queue)


#Q7:-Count even and odd numbers in that list.

List=[34,57,82,99,61,54,86,92,56,87]
count_odd=0
count_even=0
for x in List:
    if not x%2:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print('Total even no. are: ',count_even)
print('Total odd no. are: ',count_odd)



