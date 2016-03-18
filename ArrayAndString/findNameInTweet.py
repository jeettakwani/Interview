__author__='jtakwani'
'''
Given a list of names. Find whether a particular name occurs inside a given tweet or not.
If found return true otherwise false Time complexity should be less than O(n).

Ex: "Katy Perry","Ronan Keating" given as a list of string.

'''

def nameInTweet(names, tweet):

    tweet = tweet.split()
    previousWord = ''
    for word in tweet:
        if not previousWord:
            previousWord = word
            continue
        else:
            if str(previousWord + ' ' + word) in names:
                return True

        previousWord = word
    return False


names = ['Katy Perry', 'Russell Brand', 'Russel Crowe']
tweet = 'Jeet T and Hriya M make a nice couple!'

print nameInTweet(names, tweet)