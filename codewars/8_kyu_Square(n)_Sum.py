"""8 kyu Square(n) Sum
Description:

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

Arrays
Lists
Fundamentals
"""


# Oneliner with sum() and for loop
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)


# test zone
import pytest


@pytest.mark.parametrize('numbers, expected_result', [([2, 2, 2], 12), ([0, 0, 0], 0), ([-3, -3, -3], 27)])
def test_examples(numbers, expected_result):
    assert square_sum(numbers) == expected_result
