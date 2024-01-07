"""
Eyal Haimovich
January 6, 2024

PROMPT:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

INTUITION:
Retain first number in nums and remove from nums
loop through rest of nums check if any add up to target
retain new first number and repeat
Adjust index to new appropriate value

CONCLUSIONS:
Brute force method runs at O(N^2)
Using a hashmap (optimalTwoSum) we can run at O(1) time
    we retain seen nums in seen dict as we parse through nums
    if complement = target - num is true, we return i and seen index.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        curr_index = -1
        index_adjust = 0
        while nums:
            curr_num = nums.pop(0)
            curr_index += 1
            index_adjust += 1
            for index, num in enumerate(nums):
                if curr_num + num == target:
                    indices.append(curr_index)
                    indices.append(index + index_adjust)
                    return indices

    def optimalTwoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        i = 0
        while i < len(nums):
            num = nums[i]
            complement = target - num
            if complement in seen:
                return [i, seen[complement]]
            seen[num] = i
            i += 1
