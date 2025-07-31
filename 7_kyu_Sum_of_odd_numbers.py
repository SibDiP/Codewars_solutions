"""
7 kyu Sum of odd numbers
https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/discuss

Description:
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

Arrays
Lists
Mathematics
Fundamentals
"""

# 1. for-loops, list, .apend()
def row_sum_odd_numbers(n):
    number = -1
    numbers_in_line = 0
    
    for row in range(n):
        row_list = []
        numbers_in_line += 1
        for i in range(numbers_in_line):
            number += 2
            row_list.append(number)
    
    return sum(row_list)

# 2. (FC) n ** 3... yes.
def row_sum_odd_numbers(n):
    #your code here
    return n ** 3