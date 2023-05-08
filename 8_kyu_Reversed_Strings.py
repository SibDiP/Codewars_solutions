"""8 kyu Reversed Strings
https://www.codewars.com/kata/5168bb5dfe9a00b126000018

Description:

Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'

Strings
Fundamentals
"""

# 1. slice [::-1]
def solution(string):
    return string[::-1]