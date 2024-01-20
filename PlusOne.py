"""
Eyal Haimovich
January 19, 2024

PROMPT:
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in
left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]

Example 2:
Input: digits = [9]
Output: [1,0]

INTUITION:
Possible outcomes:
1) if # is not 9, add 1 to # and return digits
2) if # is 9, change to 0, and keep looping
3) if # is 9, but its first # in digits, change to 1 and append 0 to end

CONCLUSIONS:
Unless all values in digits are 9, case 3 cannot happen.
Therefore, we can simply return [1] + digits outside loop to handle it.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        # case all digits were 9
        return [1] + digits


solution = Solution()
print(solution.plusOne([9, 9, 9]))
