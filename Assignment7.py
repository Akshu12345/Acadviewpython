# Ques1
radius=float(input("enter number"))
def area(rad):
    area=3.14*rad*rad
    return area
ar=area(radius)
print(ar)


# Ques2
n=6
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        return n
    else:
        return False
for i in range(1,1001):
    print(perfect(i))


# Ques3
def multiplication(x,y=1):
    if(y==11):
        return None
    print(str(x)+"x"+str(y)+"="+str(x*y))
    multiplication(x,y+1)
multiplication(12)


# Ques4
def power(a=5,b=7):
    if(b==1):
        return a
    if(b!=1):
        return(a*power(a,b-1))
print(power())


# Ques5
dict={}
def factorial(n):
    if(n==1):
        return n
    else:
        return n*factorial(n-1)
n=int(input("enter value"))
print("factorial:",factorial(n))
a=n
b=factorial(n)
dict['number']=a
dict['fact_result']=b
print(dict)