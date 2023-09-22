# Creating a python function that takes list of numbers as input and calculates their average
# Creating Funciton
def calculate_average(*args):
    num = 0
    # Creating a for loop to calculate total values taken as input from user
    for arg in args:
        num +=1 
    sum_of_numbers = 0
    # Adding all input values to a variable using for loop
    for arg in args:
        sum_of_numbers += arg
    # Calculating average
    avg_of_numbers = (sum_of_numbers)/num
    return avg_of_numbers 
# Enter numbers and call funciton like this: calculate_average(12,65,32,34)