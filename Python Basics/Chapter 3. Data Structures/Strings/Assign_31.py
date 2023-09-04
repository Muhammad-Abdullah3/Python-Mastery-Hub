# Assignment 3.1:
# Reverse a string using at least 2 differnt methods
# The string is "FavouriteRecipe"
string = "FavouriteRecipe" # Created the string
# Method 1: Using Accessing and Slicing method
str1  = string[::-1]
# Method 2: Using Join, Reverse method
str2 = "".join(reversed(string))
# Printing out results of str1 and str2
print("Reversed string using method 1:",str1)
print("Reversed string using method 2:",str2)