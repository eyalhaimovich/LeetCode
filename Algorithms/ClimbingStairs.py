"""
Eyal Haimovich
January 20, 2024

PROMPT:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

INTUITION:
Didn't know how to approach this one.
Looking back I should manually go through to find a pattern if
I don't see it immediately.
In this case, I should have considered recursion first.

CONCLUSIONS:
Recursion is O(2^n) as it reuses previous recursions unnecessarily
Using bottom-up approach we calculate the subproblems first.
I.e., we solve from 1->n instead of n -> 1 avoiding repeat recursions.
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        first_num = 1
        second_num = 1
        total = 0
        for i in range(1, n):
            total = first_num + second_num
            first_num = second_num
            second_num = total
        return total


solution = Solution()
print(solution.climbStairs(8))
