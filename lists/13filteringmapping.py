#Using the Built-in filter and map functions
##Problem: Find the odd numbers in a list
# using a def block

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
def is_odd(x):
    """Returns True only if x is odd."""
    return x % 2 != 0
print(list(filter(is_odd, numbers)))

# or use 

print([item 
       for item in numbers 
       if is_odd(item)])
