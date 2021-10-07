#WRITE YOUR CODE IN THIS FILE
def factorial(x):
    y = 1
    for i in range(1, (x-1)):
       y = y * (x - i) 

print(factorial(5))