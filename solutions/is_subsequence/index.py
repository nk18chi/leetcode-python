# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/

# from typing import List, Dict


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer: int = 0
        tPointer: int = 0
        while sPointer < len(s) and tPointer < len(t):
            if s[sPointer] == t[tPointer]:
                sPointer += 1
            tPointer += 1
        return len(s) == sPointer
