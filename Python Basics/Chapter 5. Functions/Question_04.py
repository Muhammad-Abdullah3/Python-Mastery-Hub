# Creating a function with *kargs to print a person information
def print_person_info(**kwargs):
    Name = kwargs.get('Name','Unknown')
    Age = kwargs.get('Age','Unknown')
    City = kwargs.get('City','Unknown')
    print(f"Hello, My name is {Name}. I am {Age} years of age. I live in the city of {City}.")
# Calling the funciton
print_person_info(Name="Alexis Sanchez",Age = 28,City="Liverpool")

