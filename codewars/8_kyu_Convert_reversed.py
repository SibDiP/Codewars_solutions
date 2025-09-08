"""
8_kyu_Convert_number_to_reversed_array_of_digits.py

Codewars kata: Convert number to reversed array of digits
Level: 8 kyu
Link: https://www.codewars.com/kata/5583090cbe83f4fd8c000051

Description:
Given a non-negative integer, return an array containing a list of independent digits in reverse order.

Examples:
348597 => [7,9,5,8,4,3]
0 => [0]
1000 => [0,0,0,1]

Solutions:
"""

# 1. list comprehension, str(), int(), slice reversal
def digitize(n):
    return [int(i) for i in str(n)[::-1]]


# 2. (FC) while, .append(), n // 10
def digitize(n):
    result = []
    while n >= 1:
        result.append(n%10)
        n //= 10
    return result

# Test cases
print(digitize(35231))   # [1, 3, 2, 5, 3]
print(digitize(0))       # [0]
print(digitize(348597))  # [7, 9, 5, 8, 4, 3]
print(digitize(1000))    # [0, 0, 0, 1]
