# Ques1
import numpy as np
a=np.random.rand(10,1)
print(a)
print("Mean:-",a.mean())


# Ques2
import numpy as np
b=np.random.rand(20,1)
print(b)
print("Variance:-",b.var())
print("Standard Deviation:-",b.std())


# Ques3
import numpy as np
a=np.random.rand(10,20)
b=np.random.rand(20,25)
print("Array-1:-",a)
print("Array-2:-",b)
c=np.dot(a,b)
print("Multiply:-",c)
print("Shape of Array:-",c.shape)
print("Sum of element of array:-",np.sum(c))


# Ques4
import numpy as np
def test(x):
    return(1/(1+(np.exp(-x))))
arr=np.random.rand(10,1)
print("Random number array:-",arr)
arr=test(arr)
print("Required output:-",arr)