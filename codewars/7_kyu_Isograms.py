"""7 kyu Isograms
https://www.codewars.com/kata/54ba84be607a92aa900000f1/solutions/python?filter=me&sort=best_practice&invalids=false

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false

Strings
Fundamentals
"""


# 1. for, enumerate, O(n^2)
def is_isogram(string):
    low_string = string.lower()

    for index, val in enumerate(low_string):
        if low_string[index] in low_string[index + 1:]:
            return False

    return True


# 2. (FC) set(). O(n)
def is_isogram(string):
    return len(string) == len(set(string.lower()))
