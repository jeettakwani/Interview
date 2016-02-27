__author__ = 'jtakwani'

# @param A : string
# @param B : integer
# @return a strings
def convert(self, A, B):
    if len(A) <= 1 or B == 1:
        return A
    matrix = [[0 for x in range(len(A))] for x in range(B)]
    column = 0
    row = 0
    down = True
    for i in range(len(A)):
        matrix[row][column] = A[i]
        if row == B-1:
            down = False
        if row == 0:
            down = True
        if down:
            row += 1
        else:
            row -= 1
        column += 1
    str = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                continue
            else:
                str = str + matrix[i][j]

    return str
