"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

 

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.


"""

# 1. Pointers 

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_pointer = 0
        max_ones_sequence = 0
        
        for index, value in enumerate(nums):
            if value == 0:
                current_ones_sequence = index - start_pointer
                max_ones_sequence = max(max_ones_sequence, current_ones_sequence)
                start_pointer = index + 1
        
        max_ones_sequence = max(max_ones_sequence, len(nums) - start_pointer)
        
        return max_ones_sequence

# 2. Counter
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sequence = max_ones_sequence = 0
        
        for num in nums:
            if num:
                current_sequence += 1
            else:
                max_ones_sequence = max(max_ones_sequence, current_sequence)
                current_sequence = 0
                        
        
        return max(max_ones_sequence, current_sequence)