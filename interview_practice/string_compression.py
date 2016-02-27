__author__ = 'jtakwani'
#this proram is to compress the string
#this is 1.5 in CTCI

def compress_string(string):
    length = len(string)
    previous = string[0]
    count = 0
    compressed_string = ''
    for i in range(length):
        if string[i] != previous:
            compressed_string = compressed_string + previous + str(count)
            #print compressed_string
            count = 1
            previous = string[i]
        else:
            count += 1

    compressed_string = compressed_string + previous + str(count)

    return compressed_string

print (compress_string('aabbccccccaaaa'))