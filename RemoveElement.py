"""
Eyal Haimovich
January 17, 2024

PROMPT:
Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:

1) Change the array nums such that the first k elements of nums contain the
elements  which are not equal to val. The remaining elements of nums are not
important as well as the size of nums.

2) Return k.

INTUITION:
for loop through nums, if num != val, place it in incrementing index k

CONCLUSIONS:
Nothing new. Watch when to use nums vs range(len(nums)). Don't need an index here.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
        print(f"{k}, {nums}")
        return k
    

solution = Solution()
solution.removeElement([0,1,2,2,3,0,4,2], 2)
