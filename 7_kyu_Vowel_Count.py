'''7 kyu Vowel Count
https://www.codewars.com/kata/54ff3102c1bad923760001f3

Description:

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
Strings
Fundamentals
'''

# 1. collections.Counter, for loop
from collections import Counter


def get_count(sentence):
    vowels = ('a', 'e', 'i', 'o', 'u')
    letters = Counter(sentence)
    vowels_count = 0

    for letter in vowels:
        vowels_count += letters[letter]

    return vowels_count

# 2. (FC) sum(), in-for-in oneliner
def getCount(s):
    return sum(c in 'aeiou' for c in s)