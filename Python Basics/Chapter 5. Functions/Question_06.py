# Creating a simple funciton

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:  
# Using recursion
        return n*factorial(n-1)
# Calling function
factorial(8)