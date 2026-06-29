"""
https://www.codewars.com/kata/55cbd4ba903825f7970000f5

Grade book

Complete the function so that it finds the average of the three scores passed
to it and returns the letter value associated with that grade.

Numerical Score     Letter Grade
90 <= score <= 100  'A'
80 <= score < 90    'B'
70 <= score < 80    'C'
60 <= score < 70    'D'
0 <= score < 60     'F'

Tested values are all between 0 and 100. Theres is no need to check for negative
values or values greater than 100.
"""

# 1. Моё решение (с использованием словаря и цикла)
def get_grade(s1, s2, s3):
    grades = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}    
    average_score = sum((s1, s2, s3)) / 3
    
    for grade, min_score in grades.items():
        if average_score >= min_score:
            return grade

# 2. Решение с подсказкой ИИ (использование bisect и индексации строки)
from bisect import bisect_right

def get_grade_bisect(s1, s2, s3):
    average_score = sum((s1, s2, s3)) / 3
    breakpoints = [60, 70, 80, 90]    
    return 'FDCBA'[bisect_right(breakpoints, average_score)]