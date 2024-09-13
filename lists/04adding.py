print('Adding to a list')
c = [-45, 6, 0, 72, 1543]
print('before adding', c)
c += [10]
print('after adding', c)
letters1 = list('spam')

print('appends two items to letters1', letters1+['a','b']) # appends two items to letters1
print('unpacks Python and appends to letters1', letters1 + list("Python")) #unpacks 'Python' and appends to letters1
print('appends a copy of letters1 to letters1',letters1*2) # appends a copy of letters1 to letters1
letters1.append('a1') #appends 'a1' to letters
letters1.insert(0,123)
print('insert 123 at 0', letters1) #insert 123 at 0
a=c + c
print(a)
c.extend(['xx', 'yy'])
print('extends the list by two items',c ) #extends the list by two items
