# Creating a function that takes a number as input and returns its square
def func(n):
    result = n**2
    print(result)
# Creating a function that takes above function as an argument
def apply_function(func,num):
    func(num)
# Calling function
apply_function(func,3)