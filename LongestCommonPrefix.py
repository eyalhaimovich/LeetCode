"""
Eyal Haimovich
January 11, 2024

PROMPT:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix amongst the input strings.

INTUITION:
Find the smallest word in strs as max index (avoid invalid index)
For loop through each index
Nested for loop each word
store temp chr word[i]
If any word[i] different from temp, return output
else add temp to output and go to next index

CONCLUSIONS:
By using strs = sorted(strs), we can use the first and last words only.
Since list is sorted, the first and last words would have the most differences.
Now we only have to for loop the indexes of these two words rather than full list.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        for i in range(len(min(strs))):
            temp = ""
            for word in strs:
                if temp == "":  # first word
                    temp = word[i]
                elif word[i] != temp:
                    return output
            output += strs[0][i]
        return output

    def optimalLongestCommonPrefix(self, strs):
        output = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return output
            output += first[i]
        return output
