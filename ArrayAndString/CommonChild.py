__author__ = 'jtakwani'


def lcs():
    s = raw_input("Enter 1st String")
    r = raw_input("Enter 2nd String")
    m = len(s)
    n = len(r)
    matrix = [[0]*(5001) for i in range(5001)]
    for i in range(0,m):
        for j in range(0,n):
            if(s[i]==r[j]):
                matrix[i+1][j+1] = matrix[i][j]+1
            else:
                matrix[i+1][j+1] = max(matrix[i+1][j],matrix[i][j+1])
    print(matrix[m][n])


lcs()