"""6_kiy_Array.diff
https://www.codewars.com/kata/523f5d21c841566fde000009/solutions/python?filter=me&sort=best_practice&invalids=false

Description:
Your goal in this kata is to implement a difference function,
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in
list b keeping their order.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be
removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

Arrays
Fundamentals
Algorithms

"""


# 1. List comprehension, in/not in / for loop
def array_diff(minuend, subtrahend):
    return [num for num in minuend if num not in subtrahend]


# 2. (FC) Same but subtrahend list to set(). More efficient.
def array_diff(minuend, subtrahend):
    subtrahend_set = set(subtrahend)
    return [num for num in minuend if num not in subtrahend_set]
