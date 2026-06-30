"""
https://www.codewars.com/kata/55d24f55d7dd296eb9000030

Grasshopper - Summation

Write a program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0.

Example:
summation(8) -> 36  (1+2+3+4+5+6+7+8 = 36)
"""

# Вариант 1 (моё решение):
def summation(num):
    return sum(range(num + 1))

# Вариант 2 (AI) – формула Гаусса, O(1), целочисленное деление во избежание ошибок:
def summation_v2(num):
    return (num * (num + 1)) // 2