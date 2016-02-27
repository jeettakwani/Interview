__author__ = 'jtakwani'
class Solution:

    # @param A : string
    # @return an integer
    def atoi(self, A):
        ret = 0
        A = A.strip()
        n = len(A)
        lastNo = 0
        minus = 1
        if n == 0:
            return 0
        if A[0] == '-':
            minus = -1
            A = A[1:]
        elif A[0] == '+':
            A = A[1:]
        n = len(A)
        for i in range(n):
            if (A[i] < '0' or A[i] > '9'):
                lastNo = i-1
                break
            if i == n - 1:
                lastNo = n - 1
        if lastNo == -1:
            return 0
        A = A[:lastNo+1]
        ret = 0
        n = lastNo
        for i in range(n,-1,-1):
            ret += int(A[i])*(10**(n-i))
        ret = minus*ret
        if ret > 2147483647:
            ret = 2147483647
        elif ret < -2147483648:
            ret = -2147483648
        return ret
