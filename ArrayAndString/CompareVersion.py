__author__ = 'jtakwani'
# @param A : string
# @param B : string
#  @return an integer
def compareVersion(self, A, B):
    A = A.split('.')
    B = B.split('.')
    lenA = len(A)
    lenB = len(B)
    for i in range(lenA):
        A[i] = int(A[i])
    for i in range(lenB):
        B[i] = int(B[i])
    loopCount = min(lenA, lenB)
    for i in range(loopCount):
        if A[i] > B[i]:
            return 1
        if A[i] < B[i]:
            return -1
    if lenA > lenB:
        if sum(A[lenB:]) > 0:
            return 1
    if lenA < lenB:
        if sum(B[lenA:]) > 0:
            return -1
    return 0