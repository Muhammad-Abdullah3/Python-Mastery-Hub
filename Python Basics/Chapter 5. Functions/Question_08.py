# Creating a nested function
def outer_function(x):
    def inner_function(y):
        print(y)

    # Calling inner function inside outer function
    return inner_function(x)

# Calling function
outer_function(8)