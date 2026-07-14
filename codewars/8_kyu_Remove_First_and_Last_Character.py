# 8 kyu - Remove First and Last Character
# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
#
# It's pretty straightforward. Your goal is to create a function that removes
# the first and last characters of a string. You're given one parameter,
# the original string. You don't have to worry with strings with less than
# two characters.
#
# Срез строки s[1:-1] — самый простой и эффективный способ удалить
# первый и последний символы. Работает для строк любой длины ≥ 2.

def remove_char(s: str) -> str:
    return s[1:-1]