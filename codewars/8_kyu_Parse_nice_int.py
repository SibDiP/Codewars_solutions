"""
8_kyu_Parse_nice_int_from_char_problem.py

Codewars kata: Parse nice int from char problem
Level: 8 kyu
Link: https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1

Description:
You ask a small girl,"How old are you?" She always says, "x years old", where x is a random number between 0-9.

Write a program that returns the girl's age (0-9) as an integer.

Assume the test input string is always a valid string. For example, the input string will always be "1 years old" or "5 years old". The input string will never be "years old" without a number.

Solutions:
"""

def get_age(age):
    return int(age[0])

# Test cases
print(get_age("4 years old"))  # 4
print(get_age("9 years old"))  # 9
print(get_age("1 years old"))  # 1