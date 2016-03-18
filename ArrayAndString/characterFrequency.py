'''
For a technical phone screen:

Given a string "aaabbcccc", write a program to find the character with the second highest frequency.
'''

__author__ = 'jtakwani'
from collections import Counter

def characterFrequency(string):

    string =  Counter(string)
    print sorted(string)[-2]


def highest_frequency(arr):
  """
  Given a string "aaabbcccc", write a program to find the character with the second highest frequency.
  """
  # empty string, check input and pass non-empty string
  if not arr:
    return

  # a hash table to store values
  hashtable = {}

  # iterate through the input string and store the frequency of each character into a key-value pair in the hash table
  for elem in arr[:]:
    if elem in hashtable.keys():
      val = int(hashtable.get(elem, "none"))
      val += 1
      hashtable[elem] = val
    else:
      hashtable[elem] = 1

  # sort the hashtable by its value and grab the second highest
  output = sorted(hashtable, key=hashtable.get, reverse=False)
  return output[1]

res = highest_frequency('ababababababacccccdbdbdbaaab')
print res


characterFrequency('ababababababacccccdbdbdbaaab')