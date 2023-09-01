"""
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""



Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.

"""

# 1. (My, did't work) max(), min(), for-loop, count()
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        current_gcd_times = 0
        next_gcd_times = 0
        long_str = max(str1, str2)
        short_str = min(str1, str2)
        gcd = ''

        for i in range(1, len(short_str)+1):
            current_gcd_times = long_str.count(short_str[:i])

            if current_gcd_times > 1:
                if len(long_str) % len(short_str[:i]) == 0 and len(short_str) % len(short_str[:i]) == 0:
                    gcd = short_str[:i]
        return gcd


# 2. (Editoiral) / Brute Force | prefix check, end-to-start, min(), len()

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k or len2 % k:
                return False
            n1,n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""
