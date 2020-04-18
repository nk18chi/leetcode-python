# 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/

# from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcp(a: int, b: int):
            if a == 0:
                return b
            else:
                return gcp(b % a, a)

        d: int = gcp(len(str1), len(str2))
        return str1[:d] if str1[:d] * (len(str2) // d) == str2 and str2[:d] * (len(str1) // d) == str1 else ""
