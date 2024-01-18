"""
Eyal Haimovich
January 17, 2024

PROMPT:
Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

INTUITION:
search for needle starting at each letter of haystack
brute force approach, O(n * m) len needle * len haystack

CONCLUSIONS:
Using KMP algorithm we can reduce time to O(m+n) -> O(n)
we preprocess needle into an lps array to eliminate backtracking of haystack
i.e. ababc -> lps[00120] since ab could be start of new needle match
i.e. h=abcabababc using lps[00120]
ab[c] mismatch, n = 2, n = lps[n-1] = 0
abab[a] mismatch, n = 4, n = lps[n-1] = 2. needle[n]='a' == haysack[h]
len(ababc) == len(needle) == true
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = len(needle)
        for c in range(len(haystack)):
            if haystack[c:c+l] and \
            haystack[c:c+l] == needle:
                return c
        return -1

    def optimalStrStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)

        # Preprocessing
        pre = 0
        for i in range(1, len(needle)):
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre - 1]
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre

        # Main algorithm
        n = 0  # needle index
        for h in range(len(haystack)):
            while n > 0 and needle[n] != haystack[h]:
                n = lps[n - 1]
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1

        return -1


solution = Solution()
haystack = 'abcabababc'
needle = 'ababc'
print(solution.strStr(haystack,needle))
print(solution.optimalStrStr(haystack,needle))