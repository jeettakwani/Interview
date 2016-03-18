__author__ = 'jtakwani'

'''
write a function that has an int as input and return the equivalent String as an output

12 -> 'twelve'
4345 -> 'four thousand three hundred and forty-five'
5000000 -> five million
'''


def intToString(number,string,numberDict):

    if number > 999999:
        string = string + numberDict[number/1000000]
        number = number%1000000
        if number > 0:
            intToString(number,string,numberDict)
        else:
            print string
    elif number > 999:
        string = string + numberDict[numberDict/1000]
        number = number%1000
        if number > 0:
            intToString(number,string,numberDict)




def createDictionary():
    dict = {}

    dict[1] = 'one'
    dict[2] = 'two'
    dict[3] = 'three'
    dict[4] = 'four'
    dict[5] = 'five'
    dict[6] = 'six'
    dict[7] = 'seven'
    dict[8] = 'eight'
    dict[9] = 'nine'
    dict[10] = 'ten'
    dict[11] = 'eleven'
    dict[12] = 'twelve'
    dict[13] = 'thirteen'
    dict[14] = 'fourteen'
    dict[15] = 'fifteen'
    dict[16] = 'sixteen'
    dict[17] = 'seventeen'
    dict[18] = 'eighteen'
    dict[19] = 'nineteen'
    dict[20] = 'twenty'
    dict[30] = 'thirty'
    dict[40] = 'fourty'
    dict[50] = 'fifty'
    dict[60] = 'sixty'
    dict[70] = 'seventy'
    dict[80] = 'eighty'
    dict[90] = 'ninety'
    dict[100] = 'hundred'
    dict[1000] = 'thousand'
    dict[100000] = 'lakh'
    dict[1000000] = 'million'

    return dict

numberDict = createDictionary()
intToString(50000,'',numberDict)