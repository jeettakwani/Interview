'''
You have n - 1 numbers from 1 to n. Your task is to find the missing number.

I.e.
n = 5
v = [4, 2, 5, 1]
The result is 3.
'''

def findMissingNumber(numbers):
    n = max(numbers)

    totalSum = (n * (n+1))/2

    arraysum = sum(numbers)

    print totalSum-arraysum


findMissingNumber([4,2,5,1,3,7,12,14,11,15,6,8,9,10])