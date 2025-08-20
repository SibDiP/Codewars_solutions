"""
8_kyu_get_character_from_ASCII_Value.py

Codewars kata: get character from ASCII Value
Level: 8 kyu

Description:
Write a function get_char() which takes a number and returns the corresponding ASCII char for that value.

Example:
get_char(65) returns 'A'

Solutions:
"""

# Solution 1: Alternative (same approach, just more explicit)
def get_char(c):
    """Convert ASCII number to character"""
    return chr(c)

# Test cases
print(get_char(65))   # 'A'
print(get_char(97))   # 'a'
print(get_char(48))   # '0'
print(get_char(32))   # ' ' (space)
print(get_char(33))   # '!'
