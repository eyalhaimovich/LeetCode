"""
Eyal Haimovich
January 6, 2024

PROMPT:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

INTUITION:
Initially I thought of using a hashmap to record which parenthesis was first,
but that approach is unnecessary and complex.
I realized I can simply store the parenthesis in a stack and call the most recent.

Steps:
Create Dict with '(' : ')' to store the pair
for loop through str
if c is a key, add to stack
else if stack not empty and == matching appropriate dict value pop from stack
if stack is empty, return true else false

CONCLUSIONS:
I used string recent = ''
It is a better approach in both time and space complexity to use stack = []
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par_dict = {'(': ')', '[': ']', '{': '}'}
        recent = ''
        for c in s:
            if c in par_dict:
                recent += c
            elif recent and c == par_dict[recent[-1]]:
                recent = recent[:-1]
            else: # if wrong parenthesis closed
                return False

        # if not all parenthesis are closed
        return not recent


class Solution(object):
    def optimalIsValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par_dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in par_dict:
                stack.append(c)
            elif stack and c == par_dict[stack.pop()]:
                continue
            else:  # if wrong parenthesis closed
                return False

        # if not all parenthesis are closed
        return not stack

