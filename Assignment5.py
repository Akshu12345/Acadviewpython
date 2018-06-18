# Ques1
a=int(input("enter any year"))
if(a%4==0):
    print("year is leap year")
else:
    print("year is not leap year")


# Ques2
a=input("enter value of a")
b=input("enter value of b")
if(a==b):
    print("square")
else:
    print("rectangle")


# Ques3
x=input("enter the age of x ")
y=input("enter the age of y ")
z=input("enter the age of z ")
if(x>y and x>z):
    print("x is oldest")
elif(y>x and y>z):
    print("y is oldest")
else:
    print("z is oldest")
if(x<y and x<z):
    print("x is youngest")
elif(y<x and y<z):
    print("y is youngest")
else:
    print("z is youngest")


# Ques4
a=int(input("enter any value between 1 to 200"))
if(a<=50):
    print("Sorry! No prize this time")
elif(a>=51 and a<=150):
    print("You won a wooden dog!")
elif(a>=151 and a<=180):
    print("You won a book!")
elif(a>=181 and a<=200):
    print("You won chocolate")
else:
    print("wrong choice")


# Ques5
q=int(input("Enter the purchase quantity"))
if(q<10):
    c=q*100
    print("Total cost is ",a)
else:
    cost=q*100
    final_cost=(cost*10)/100
    total_cost=cost-final_cost
    print("total cost after discount: ",total_cost)




