# Creating a funciton to sum all arguments given in the funciton using * args
def sum_all(*args):
    sum = 0
    for arg in args:
        sum+=arg
    print("Sum of all numbers is:",sum)
    return sum
# Calling the function
sum_all(12,76,-23,98,-1298,342,12,982,3)