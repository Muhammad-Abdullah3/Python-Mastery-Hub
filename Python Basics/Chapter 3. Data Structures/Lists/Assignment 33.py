# Reverse list by using 2 different methods
# Creating 2 lists
list1 = ["Sharif","Shaw","is","in","the","house."]
list2 = [34,5,77,8,99,10,1923]
## Method 1
# Using Reverse()
print("Initial List 1:",list1)
reversed_list1 = list1.reverse()
print("Reversed List 1:", reversed_list1)
## Method 2
# Using The reversed()
# This returns an iterator which can be converted into a list
print("Initial List 2:",list1)
reversed_list2 = list(reversed(list2))
print("Reversed List 1:", reversed_list2)

