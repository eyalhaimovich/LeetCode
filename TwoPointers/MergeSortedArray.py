"""
Eyal Haimovich
January 23, 2024

PROMPT:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two
integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first
m elements denote the elements that should be merged, and the last n elements are set to 0
and should be ignored. nums2 has a length of n.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

INTUITION:
Immediate thought was:
If nums1[i] >nums2[j], place nums1[i] in temp and compare min(nums2[k], temp)
Place that # in nums1[i]
This would work, but would require a lot of if statements, conditions, etc.

CONCLUSIONS:
Use "two pointers", similar to initial approach, keep track of nums1/2 and fill backwards
Instead, since we are given n & m, use them to index the arrays and fill nums1[i] backwards
Loop through the indexes of m-1 & n-1 until emptied (all #s compared)
"""


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    i = m + n - 1
    a = m - 1
    b = n - 1

    while b >= 0:
        if a >= 0 and nums1[a] > nums2[b]:
            nums1[i] = nums1[a]
            a -= 1
        else:
            nums1[i] = nums2[b]
            b -= 1
        i -= 1


nums1 = [1, 2, 3, 0, 0, 0]
merge(nums1, 3, [2, 5, 6], 3)
print(nums1)

