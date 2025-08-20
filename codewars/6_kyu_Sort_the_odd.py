"""6 kyu Sort the Odd
url:https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

Description:
Task

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
Examples

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

Fundamentals
Arrays
Sorting
"""

def sort_array(source_array):
    odd_list = []
    odd_list_pointer = 0

    for i in source_array:
        if i % 2 != 0:
            odd_list.append(i)
    odd_list.sort()
    
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd_list[odd_list_pointer]
            odd_list_pointer += 1
    
    return source_array