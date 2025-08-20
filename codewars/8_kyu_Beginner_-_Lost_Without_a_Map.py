"""
8 kyu Beginner - Lost Without a Map

Description:

Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
Fundamentals
Arrays
"""

# 1. list comprehansion
def maps(a):
    return [i*2 for i in a]