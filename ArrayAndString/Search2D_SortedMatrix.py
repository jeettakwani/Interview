__author__ = 'jtakwani'

def searchMatrix(matrix,element):

    rows = len(matrix)
    column = len(matrix[0])-1
    i = 0
    j = column
    while i < rows and j > 0:
        if matrix[i][j] == element:
            return "found in row: " + str(i+1) + " and column: " + str(j+1)
        elif matrix[i][j] > element:
            j -= 1
        else:
            i += 1
    return "not found"

print [[1,2,3],
       [4,5,6],
       [7,8,9],
       [10,11,12]]
print searchMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]],11)