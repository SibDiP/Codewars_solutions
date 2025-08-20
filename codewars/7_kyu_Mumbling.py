'''Description:
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python

This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
Fundamentals
Strings
Puzzles
'''

# 1. for loop oneliner, enumerate(), join(), .capitalize().

def accum(s):
    return '-'.join((value*(count+1)).capitalize() for count, value in enumerate(s))
