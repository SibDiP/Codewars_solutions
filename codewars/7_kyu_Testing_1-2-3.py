"""
7_kyu_Testing_1-2-3.py

Codewars kata: Testing 1-2-3
Level: 7 kyu

Description:
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples:
number(["a", "b", "c"]) --> ["1: a", "2: b", "3: c"]
number([]) --> []

Solutions:
"""


# Solution 1: list comprehansion, enumerate() with start parameter (Python 3.2+)
def number(lines):
    return [f"{i}: {line}" for i, line in enumerate(lines, start=1)]

# Test cases
print(number(["a", "b", "c"]))  # ["1: a", "2: b", "3: c"]
print(number([]))               # []
print(number(["hello", "world", "python"]))  # ["1: hello", "2: world", "3: python"]
