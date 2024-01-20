"""
Eyal Haimovich
January 19, 2024

PROMPT:
Given a string s consisting of words and spaces,
return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

INTUITION:
return len(s.split()[-1])
easiest approach, but goes over entire string unnecessarily


CONCLUSIONS:
while loop for whitespace on backend
then while loop until whitespace appears
only needs to traverse s until last word is done
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i-=1
        while i >= 0 and s[i] != ' ':
            l+=1
            i-=1
        return l


solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
