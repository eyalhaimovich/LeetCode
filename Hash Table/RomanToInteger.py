"""
Eyal Haimovich
January 6, 2024

PROMPT:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

INTUITION:
Create a dictionary for symbols
loop through each symbol in s
retain previous symbol after each loop as 'last symbol' to check for subtraction
use elif for each of the 6 possible instances of subtraction
if instance occurs, adjust the addition by appropriate amount
for example IV = 4, since we already added 1 for I, only add 3 for V.

CONCLUSIONS:
A better approach is to check next symbol rather than previous symbol.
if the next symbol is > current symbol, current symbol should simply subtract.

"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        total = 0
        lval = ''
        for i in s:
            # subtract conditions
            if i == 'V' and lval == 'I':
                total += 3
            elif i == 'X' and lval == 'I':
                total += 8
            elif i == 'L' and lval == 'X':
                total += 30
            elif i == 'C' and lval == 'X':
                total += 80
            elif i == 'D' and lval == 'C':
                total += 300
            elif i == 'M' and lval == 'C':
                total += 800
            else:
                total += roman_dict[i]
            # set last char
            lval = i

        return total

    def optimalRomanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0

        for i in range(len(s)):
            # if i is not last symbol and next symbol is larger, use subtraction.
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]

        return ans