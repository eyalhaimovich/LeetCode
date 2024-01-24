"""
Eyal Haimovich
January 19, 2024

PROMPT:
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [1,3,5,6], target = 5
Output: 2

INTUITION:
Binary Search
Compare middle index to first and last.
Adjust left or right index to the middle index, cutting array in half.
Keep going until mid == target, else return left index ().

CONCLUSIONS:
Use binary search in a SORTED list/data
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l


solution = Solution()
print(solution.searchInsert([2,3,5,7,8,9], 7))
