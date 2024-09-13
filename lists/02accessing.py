c = [-45, 6, 0, 72, 1543]
c[0]
c[4]
c[-1] # same as last item
c[-5]
number1, number2, number3 = [2, 3, 5] #unpacks to list items
print('Unpacked numbers')
print(number1, number2, number3)
print('Iterate through a list using for loop')
print(len(c))
for i in range(len(c)):
    print(c[i])
