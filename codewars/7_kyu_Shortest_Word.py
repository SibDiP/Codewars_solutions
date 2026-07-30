"""
Shortest Word
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.

Strings
Fundamentals
"""


# 1. One-liner using min() with key=len — O(n) time, O(n) space
def find_short(s: str) -> int:
    return len(min(s.split(), key=len))


# 2. Manual loop tracking smallest length — O(n) time, O(n) space
def find_short(s: str) -> int:
    words = s.split()
    smallest = len(words[0])
    for word in words:
        if len(word) < smallest:
            smallest = len(word)
    return smallest
