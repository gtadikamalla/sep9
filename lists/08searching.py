numbers = [3, 7, 1, 4, 2, 8, 5, 6, 3, 5, 6, 7]
print('numbers', numbers)
print('index of first element that matches 5', numbers.index(5)) # index of first element that matches 5
print('find index of 5 starting from position 4', numbers.index(3,2)) #find index of 5 starting from position 4
print('find position of 7 between 0 and 4', numbers.index(7, 0, 4)) #find position of 7 between 0 and 4
print('using the in operator, returns boolean', 8 in numbers) #using the in operator, returns boolean
print('using the in operator, returns boolean', 8 not in numbers)
print('returns number of 3s in the list', numbers.count(3)) # returns number of 3s in the list
