#Removing from a list ===
letters1 = list('spam')
c = [-45, 6, 0, 72, 1543]
popped = c.pop()
c = [-45, 6, 0, 72, 1543]
print('removes the item at index 1; list is shorter now', popped, ' is returned')
  #removes the item at index 1; list is shorter now
print("finds and removes first occurrence of 'y'")
letters1.remove('s') #finds and removes first occurrence of 'y'
print(letters1)
print('deletes the item at 0 position')
del c[0]  #deletes the item at 0 position
print(c)
c = [-45, 6, 0, 72, 1543]
print('Removes items at positions 0 and 1')
del c[0:2] #Removes items at positions 0 and 1
print(c)
c = [-45, 6, 0, 72, 1543]
print('list', c)
print('find index of 0')
print(c.index(0))
print('removes the item 72 and resizes the list')
c.remove(72) #removes the item and resizes the list
print(c)
print('empties the list')
c.clear() #empties the list
print(c)
# comparing lists
