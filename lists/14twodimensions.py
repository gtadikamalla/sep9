#Lists can contain other lists as elements.
#Typical use is to represent tables of values consisting of information arranged in rows and columns.
#To identify a particular table element, we specify two indices—the first identifies the element’s row, the second the element’s column.
matrix1 = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]

#Iterating through the elements
for i, row in enumerate(matrix1):
    for j, item in enumerate(row):
        print(f'matrix1[{i}][{j}]={item} ', end=' ')
    print()
#Outer for statement iterates over the list’s ows one row at a time.
#During each iteration of the outer for statement, the inner for statement iterates over each column in the current row.

# for i, row in enumerate(matrix1):
#     for j, item in enumerate(row):
#         print('matrix1[{}][{}]={} '.format(i, j, item), end=' ')
#     print()
