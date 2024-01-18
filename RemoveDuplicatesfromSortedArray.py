"""
Eyal Haimovich
January 17, 2024

PROMPT:
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted,

you need to do the following things:
1) Change the array nums such that the first k elements of nums contain the unique
elements in the order they were present in nums initially. The remaining elements
of nums are not important as well as the size of nums.

2) Return k.

Example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

INTUITION:
We for loop through the nums list and keep track of previously seen nums.
if i is not in nums, we add it to seen list, replace nums[k], and increment k.

CONCLUSIONS:
Need to make use of the list being sorted.
Since sorted, we only need to compare i to i-1, a unique # cannot repeat.
Compare to i-1 to allow checking last num without dealing with index overflow.
i.e. [5,6,5] cannot happen, therefore, we don't need a seen list and can
replace in-place without a test for seen.
Reduces time from O(n^2) to O(n) and space from O(n) to O(1).
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = []
        c = 0
        for i in nums:
            if i not in seen:
                seen.append(i)
                nums[c] = i
                c+=1
        print(f"{c}, {nums}")
        return c

    def optimalRemoveDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1  # nums[0] always unique, start at index 1
        for i in range(1, len(nums)):  # nums[0] always unique, start at index 1
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        print(f"{k}, {nums}")
        return k


solution = Solution()
solution.removeDuplicates([1,1,1,2,4,4,5])
solution.optimalRemoveDuplicates([1,1,1,2,4,4,5])
