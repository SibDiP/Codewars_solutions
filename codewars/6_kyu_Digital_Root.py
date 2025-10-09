"""
6_kyu_Sum_of_Digits_Digital_Root.py

Codewars kata: Sum of Digits / Digital Root
Level: 6 kyu
Link: https://www.codewars.com/kata/541c8630095125aba6000c00/

Description:
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.

Examples:
16 --> 1 + 6 = 7
942 --> 9 + 4 + 2 = 15 --> 1 + 5 = 6
132189 --> 1 + 3 + 2 + 1 + 8 + 9 = 24 --> 2 + 4 = 6
493193 --> 4 + 9 + 3 + 1 + 9 + 3 = 29 --> 2 + 9 = 11 --> 1 + 1 = 2

Solutions:
"""

# Solution 1: Mathematical approach using modulo 9
def digital_root(n: int) -> int:
    return (0 if n == 0 
            else 9 if n % 9 == 0 
            else n % 9)

# Solution 2: Clever one-liner from comments (FC)
def digital_root_oneliner(n):
    return n % 9 or n and 9

# Test cases
print(digital_root(16))      # 7
print(digital_root(942))     # 6
print(digital_root(132189))  # 6  
print(digital_root(493193))  # 2
print(digital_root(0))       # 0
