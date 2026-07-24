# 8 kyu - Removing Elements
# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2
#
# Take an array/list and remove every second element from the array/list.
# Always keep the first element and start removing with the next element.
# Example:
#   ["Keep", "Remove", "Keep", "Remove", "Keep"] → ["Keep", "Keep", "Keep"]
#
# Срез с шагом 2 — самый простой и эффективный способ выбрать элементы
# с чётными индексами (0, 2, 4, ...), тем самым удаляя каждый второй элемент.

def remove_every_other(my_list):
    return my_list[::2]