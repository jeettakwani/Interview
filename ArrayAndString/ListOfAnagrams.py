__author__ = 'jtakwani'

from collections import defaultdict

def listOfAnagrams():
    n = input("ENter number of strings")
    words = []
    for i in range(n):
        s = raw_input()
        words.append(s)

    dictionaryOfAnagrams = defaultdict(list)


    for i in range(len(words)):
        word = ''.join(sorted(words[i]))
        if word not in dictionaryOfAnagrams:
            print word
            dictionaryOfAnagrams[word].append(words[i])
        else:
            dictionaryOfAnagrams[word].append(words[i])

    for i,j in dictionaryOfAnagrams.iteritems():
        print dictionaryOfAnagrams[i],


listOfAnagrams()