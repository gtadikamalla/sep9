#Like list comprehensions, but create iterable generator objects that produce values on demand.
#Known as lazy evaluation.
#For large numbers of items, creating lists can take substantial memory and time.
#Generator expressions can reduce memory consumption and improve performance if the whole list is not needed at once.

#create a list of square of odd numbers in a list
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
# for value in (x ** 2 for x in numbers if x % 2 != 0):
#     print(value, end='  ')

#create a list of square of odd numbers in a list using a generator
squaresOfOdds = (x ** 2 
                 for x in numbers 
                 if x % 2 != 0)

print([i for i in squaresOfOdds])

