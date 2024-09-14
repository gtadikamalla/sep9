#a lambda is an in-line function
# For simple functions like is_odd that return only a single expression’s value, 
# you can use a lambda expression (or simply a lambda) to define the function inline.

#A lambda expression is an _anonymous function
#Begins with the lambda keyword followed by a comma-separated parameter list, 
# a colon (:) and an expression.
#A lambda implicitly returns its expression’s value.



numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
print(list(filter(lambda x: x % 2 != 0, numbers)))

#Another lambda example
#Problem: Square the numbers in a list
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
print(list(map(lambda x: x ** 2, numbers)))
#Function map’s first argument is a function that receives one value and returns a new value.
#equivalent list comprehension: [item ** 2 for item in numbers]

#More lambda example
#Find squares of odd numbers from a list

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
print(list(
         filter(lambda x: x % 2 != 0,map(lambda x: x ** 2,  numbers))))

#Equivalent list comprehension:  [x ** 2 for x in numbers if x % 2 != 0]
