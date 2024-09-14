# def add(a):
#     x=a+5
#     return (x) 


# addition=add(5)
# print(addition)


# c=['a','b','c']
# del c
# print(c)

new_list=['I eat '+ fruit for fruit in ('apple','banana','kiwi')]
new_list0=['I eat '+ fruit for fruit in 'apple']
new_list2=['I eat '+ fruit for fruit in '1234']
#new_list3=['I eat '+ fruit for fruit in 1234] -- 
# Error, do not enter number in for loop, 1234 is an integer, which is not iterable. 
# The for loop in a list comprehension expects an iterable object, like a list, string, tuple, etc.

# new_list2=['I eat '+ fruit for fruit in int(1234)]

# new_list1=[x-1 
#            for x in range(1,10)
#            if x%2==0]
# print(new_list)
# print(new_list1)
# print(new_list0)
# print(new_list2)
# #print(new_list3)

list2=['Ganga', 'Ganesh','Amma','Nanna']

print('The position is', list2.index('Ganga'))

list1= list(range(10))
print(list1)

list9=[10 if x==2 else x 
       for x in list1]
print(list9)

numbers = list(range(15))
print('numbers: ', numbers)