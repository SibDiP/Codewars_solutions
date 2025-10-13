"""
7_kyu_Basic_Sequence_Practice.py

Codewars kata: Basic Sequence Practice
Level: 7 kyu
Link: https://www.codewars.com/kata/5436f26c4e3d6c40e5000282

Description:
A function that takes an integer n and returns a list/array of length abs(n) + 1 of the cumulative sum.

For example:
sum_of_n(5) => [0, 1, 3, 6, 10, 15]
sum_of_n(-5) => [0, -1, -3, -6, -10, -15]
sum_of_n(0) => [0]

For n > 0: 0, 1, 1+2, 1+2+3, ..., 1+2+3+...+n
For n < 0: 0, -1, -1-2, -1-2-3, ..., -1-2-3-...-n
For n = 0: 0

Solutions:
"""

# My solution: Iterative approach with edge case handling
def sum_of_n(n: int) -> list[int]:
    if n == 0:
        return [0]
    
    result = [0]
    abs_n = abs(n)
    
    for i in range(1, abs_n + 1):
        result.append(result[-1] + i)
        
    return ([-num for num in result] if n < 0 else result)


# Solution 2 (AI): Mathematical approach using triangular numbers
def sum_of_n_math(n: int) -> list[int]:
    if n == 0:
        return [0]
    
    abs_n = abs(n)
    result = [i * (i + 1) // 2 for i in range(abs_n + 1)]
    
    return [-num for num in result] if n < 0 else result

# Test cases
print(sum_of_n(5))   # [0, 1, 3, 6, 10, 15]
print(sum_of_n(-5))  # [0, -1, -3, -6, -10, -15]
print(sum_of_n(0))   # [0]
print(sum_of_n(3))   # [0, 1, 3, 6]
print(sum_of_n(-3))  # [0, -1, -3, -6]
