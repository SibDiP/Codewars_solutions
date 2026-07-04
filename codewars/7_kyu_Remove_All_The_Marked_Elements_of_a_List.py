# 7 kyu - Remove All The Marked Elements of a List
# https://www.codewars.com/kata/563089b9b7be13472e00001b
#
# Define a method/function that removes from a given list of integers all the 
# values contained in a second list. The method should return a new list.
# Example:
#   integer_list = [1, 1, 2, 3, 1, 2, 3, 4]
#   values_list = [1, 3]
#   result = [2, 2, 4]
#
# Решение использует множество для значений, которые нужно удалить, 
# для ускорения проверки вхождения (O(1) вместо O(n)).
# List comprehension — читаемый и эффективный способ фильтрации.

class List:
    def remove_(self, integer_list, values_list) -> list:
        values_set = set(values_list)
        return [integer for integer in integer_list if integer not in values_set]