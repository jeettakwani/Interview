'''
Given an array with numbers, your task is to find 4 numbers that will satisfy this equation:
A + B + C = D
'''

def sum4(numbers):

    dict = {}

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            sum = numbers[i] + numbers[j]
            dict[sum] = [i,j]

    flag = 'not'
    for i in range(len(numbers)):

        for j in range(len(numbers)):
            set1 = set()
            diff = -numbers[i] + numbers[j]
            if diff in dict:
                index = dict[diff]
                set1.add(str(numbers[i]))
                set1.add(str(numbers[j]))
                set1.add(str(numbers[index[0]]))
                set1.add(str(numbers[index[1]]))

                if len(set1) != 4:
                    continue
                else:
                    flag = 'found'
                    print set1
                    break
            if flag == 'found':
                break

sum4([1,3,2,4,7])