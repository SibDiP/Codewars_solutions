"""6_kyu_Duplicate_Encoder.py
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/solutions/python?filter=me&sort=best_practice&invalids=false

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
Examples

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("

Notes

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
Strings
Arrays
Fundamentals
"""

# 1. collections.Counter()

from collections import Counter


def duplicate_encode(word):
    result_str = ''
    word_lower = word.lower()
    letter_dict = dict(Counter(word_lower))

    for i in word_lower:
        if letter_dict[i] == 1:
            result_str += '('
        else:
            result_str += ')'

    return result_str
