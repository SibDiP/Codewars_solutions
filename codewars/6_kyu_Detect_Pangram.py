"""6 kyu Detect Pangram
https://www.codewars.com/kata/545cedaa9943f7fe7b000048

Description:

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

Strings
Data Structures
Fundamentals
"""


# 1. for, if, rfind(), chr(), unicode_index
def is_pangram(s):
    s = s.lower()
    for unicode_index in range(97, 123):
        print(unicode_index)
        if s.rfind(chr(unicode_index)) == -1:
            return False
    return True


# 2. (FC) import string, oneliner, set(), issubset(), string.ascii_lowercase
import string


def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))
