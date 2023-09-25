# Creating a funciton that perform composition of two functions
# Creating first funciton f
def f(x):
    fun1 = x*2+4
    return fun1
# Creating second function g
def g(x):
    fun2= x+5*(x**2)-1
    return fun2
# Creating a function to do composition
def compose(f,g):
    # Taking the input for value of x
    x_str = input("Enter the value:")
    x = float(x_str)# Converting the string value to float
    # Composition of function
    return f(g(x))

# Calling Compose function
compose(f,g)

