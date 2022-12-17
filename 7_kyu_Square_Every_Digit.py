"""7 kyu Square Every Digit
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
Mathematics
Fundamentals
"""


# 1. oneline-for loop, .join(),

def square_digits(num):
    return int(''.join(str(int(x) ** 2) for x in str(num)))


# test zone
import pytest


@pytest.mark.parametrize('number, expected_result', [(164, 13616), (2, 4), (000, 0)])
def test_examples(number, expected_result):
    assert square_digits(number) == expected_result
