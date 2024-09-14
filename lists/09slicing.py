numbers = list(range(15))
print('numbers: ', numbers)
print(numbers[2:6]) # get entries from item 2 to item 6, excluding 6
print(numbers[:6]) # Starting from 0, go up to item 6
print(numbers[6:]) # starting from 6, all items after that
print(numbers[::2]) #Get every second item
print(numbers[2::])
print(numbers[::-1]) #starting from 0 go -1 index at a time
print(numbers[-1:])
numbers[0:3] = ['one', 'two'] #replace the first
print('numbers: ', numbers)

