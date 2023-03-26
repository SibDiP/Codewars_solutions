"""Valid Mountain Array
https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true



Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 104


It's very easy to keep track of a monotonically increasing or decreasing ordering of elements. You just need to be
able to determine the start of the valley in the mountain and from that point onwards, it should be a valley i.e. no
mini-hills after that. Use this information in regards to the values in the array and you will be able to come up
with a straightforward solution."""

# 1. while loop, walk up - walk down
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        pointer = 0
        arr_len = len(arr)

        if arr_len < 3:
            return False
        # walk up
        while pointer < arr_len - 1:
            if arr[pointer] < arr[pointer + 1]:
                pointer += 1
            else:
                break

        if pointer == 0 or pointer == arr_len - 1:
            return False
        # walk down
        while pointer < arr_len - 1:
            if arr[pointer] > arr[pointer + 1]:
                pointer += 1
            else:
                return False

        return True






