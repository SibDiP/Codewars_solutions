"""
8_kyu_Find_Maximum_and_Minimum_Values_of_a_List.py

Codewars kata: Find Maximum and Minimum Values of a List
Level: 8 kyu
Link: https://www.codewars.com/kata/577a98a6ae28071780000989

Description:
Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and smallest number in that list, respectively.

Solutions:
"""

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

# Test cases
print(minimum([-52, 56, 30, 29, -54, 0, -110]))  # -110
print(maximum([-52, 56, 30, 29, -54, 0, -110]))  # 56
print(minimum([42, 54, 65, 87, 0]))  # 0
print(maximum([42, 54, 65, 87, 0]))  # 87