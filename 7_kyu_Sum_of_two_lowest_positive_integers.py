"""Sum of two lowest positive integers
https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive
integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
Arrays
Fundamentals
"""


# 1. sorted(), sum(), O(n log n)
def sum_two_smallest_numbers(numbers):
    sorted_nums = sorted(numbers)
    return sum(sorted_nums[:2])

# 2. smallest & sec_smallest, for, sum(), O(n)
def sum_two_smallest_numbers(numbers):
    smallest = float('inf')
    second_smallest = float('inf')

    for num in numbers:

        if num < smallest:
            second_smallest = smallest
            smallest = num

        elif num < second_smallest:
            second_smallest = num

    return sum([smallest, second_smallest])
