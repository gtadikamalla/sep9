#Mapping is a common functional-style programming operation that produces a result 
# with the same number of elements as the original data being mapped.
# list3 = [item ** 2 for item in range(1, 6)]
# print(list3)


def square(a):
    return a**2

y=list(map(square,range(1,6)))
print(y)