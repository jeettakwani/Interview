__author__ = 'jtakwani'

import re
def reviewCorpusSplit():

    sentence = input("Enter a sentence upto 3 lines")
    print sentence.replace('!','.').replace('?','.').replace('...','.').split('. ')


reviewCorpusSplit()