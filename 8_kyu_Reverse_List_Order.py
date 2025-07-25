"""
8_kyu_Reverse_List_Order.py

Description:

In this kata you will create a function that takes in a list and returns a list with the reverse order.
Examples (Input -> Output)

* [1, 2, 3, 4]  -> [4, 3, 2, 1]
* [9, 2, 0, 7]  -> [7, 0, 2, 9]

Lists
Fundamentals
"""

# 1. [::-1]
def reverse_list(l):
    return l[::-1]