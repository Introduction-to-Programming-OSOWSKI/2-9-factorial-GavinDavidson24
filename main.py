#WRITE YOUR CODE IN THIS FILE
def factorial(x):
    total= 1

    for i in range(x, 1, -1):
        total = total * i

    return total



print(factorial(10))
