"""
https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3257/
Given an Array of integers, return an Array where every element at an even-indexed position is squared.

Input: array = [9, -2, -9, 11, 56, -12, -3]
Output: [81, -2, 81, 11, 3136, -12, 9]
Explanation: The numbers at even indexes (0, 2, 4, 6) have been squared,
whereas the numbers at odd indexes (1, 3, 5) have been left the same.
"""


def square_even(arr: list[int]) -> list[int]:

    for i, v in enumerate(arr):
        if i % 2 == 0:
            arr[i] = v ** 2
        else:
            pass
    return arr


array = [9, -2, -9, 11, 56, -12, -3]
print(square_even(array))
