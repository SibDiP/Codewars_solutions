"""7 kyu Beginner Series #3 Sum of Numbers

Description:
Given two integers a and b, which can be positive or negative,
find the sum of all the integers between and including them
and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!
Examples (a, b) --> output (explanation)

(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

Fundamentals
Algorithms"""


# 1. oneliner, sum(), range(), for loop, min(), max()
# Here I didn't know how range exactly works.
def get_sum(a, b):
    return sum(x for x in range(min(a, b), max(a, b) + 1))


# 2. oneliner, sum(), range(), min(), max()
# almost same, but no for loop. range() - returns a iterable class 'range'.

def get_sum2(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


# test zone
import pytest


@pytest.mark.parametrize('a, b, expected_result', [(0, 1, 1),
                                                   (0, 0, 0),
                                                   (-50, 0, -1275)])
def test_example(a, b, expected_result):
    assert get_sum(a, b) == expected_result


@pytest.mark.parametrize('a, b, expected_result', [(0, 1, 1),
                                                   (0, 0, 0),
                                                   (-50, 0, -1275)])
def test_example2(a, b, expected_result):
    assert get_sum2(a, b) == expected_result
