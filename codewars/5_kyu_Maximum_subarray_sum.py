# Maximum subarray sum (5 kyu)
# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
#
# Instructions:
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or
# list of integers:
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) # should be 6: [4, -1, 2, 1]
#
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
# If the list is made up of only negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid
# sublist/subarray.

# My solution (not effective one)
def max_sequence(arr):
    max_sum = 0
    len_arr = len(arr)

    if len_arr == 0:
        return 0

    # Start num loop
    for start_num in range(len_arr):
        print(start_num)

        # Sequence loop
        for end_of_num in range(start_num + 1, len_arr + 1):
            cur_sequence = arr[start_num:end_of_num]
            cur_sum = 0

            for i in range(len(cur_sequence)):
                cur_sum += cur_sequence[i]

            if cur_sum > max_sum:
                max_sum = cur_sum

    if max_sum == 0:
        return max_sum

    return max_sum


print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))


# Kadane’s Algorithm | O(n)
def max_sequence(arr):
    max_so_far = 0
    max_ending_here = 0

    for num in arr:
        max_ending_here += num
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
