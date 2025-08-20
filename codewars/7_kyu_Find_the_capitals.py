"""
7_kyu_Find_the_capitals.py
https://www.codewars.com/kata/539ee3b6757843632d00026b/solutions/python?filter=me&sort=best_practice&invalids=false

Description
Instructions

Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.
Example (Input --> Output)

"CodEWaRs" --> [0,3,4,6]

Strings
Arrays
Fundamentals
"""

# 1. list comprehansion, range(len()), str.isupper()
def capitals(word):
    return [i for i in range(len(word)) if word[i].isupper()]

# 2. (FC) better | list comprehansion, enumerate(), str.isupper()
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]