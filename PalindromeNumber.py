"""
Eyal Haimovich
January 6, 2024

PROMPT:
Given an integer x, return true if x is a palindrome, and false otherwise.

INTUITION:
convert int to str, flip it, and compare to original.

CONCLUSIONS:
To retain as int, use % 10 alongside // int division to compare original num vs. reversed num
if it is a palindrome,
    even -> x == reversed_num
    odd -> reversed_num // 10 ignoring middle digit

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

    def optimalIsPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # -nums or ending in 0 can't be palindrome
        if x <= 0 or x % 10 == 0:
            return False

        reversed_num = 0
        original = x

        while x > reversed_num:
            # retain last digit of x
            reversed_num = reversed_num * 10 + x % 10
            # remove last digit x
            x //= 10

        # first condition for even, second condition for odd
        return x == reversed_num or x == reversed_num // 10
