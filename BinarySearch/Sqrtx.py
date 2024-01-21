"""
Eyal Haimovich
January 20, 2024

PROMPT:
Given a non-negative integer x, return the square root of x rounded down
to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842...,
and since we round it down to the nearest integer, 2 is returned.

INTUITION:
We are looking for an int between 0 to x that is closet to x*x
run a binary tree between 0 to x, comparing mid*mid <=> x
return right as we are rounding down, not up.

CONCLUSIONS:
Always think if the problem involves a sorted list of integers.
If so, binary should be considered immediately.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid < x:
                l = mid + 1
            elif mid * mid > x:
                r = mid - 1
            else:
                return mid
        return r


solution = Solution()
print(solution.mySqrt(32))
