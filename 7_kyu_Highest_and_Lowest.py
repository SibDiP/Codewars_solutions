"""7 kyu Highest and Lowest
https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

Discription:
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
Examples

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes

    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, and highest number is first.
"""


# map(), f-string, max(), min()
def high_and_low(numbers):
    int_list = list(map(int, numbers.split()))
    return f"{max(int_list)} {min(int_list)}"


# test_zone
import pytest


@pytest.mark.parametrize('numbers, expected_result', [("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6", "542 -214"),
                                                      ("1 1 0", "1 0"),
                                                      ("0", "0 0")])
def test_examples(numbers, expected_result):
    assert high_and_low(numbers) == expected_result
