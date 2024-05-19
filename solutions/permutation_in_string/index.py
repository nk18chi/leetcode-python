# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target: List[int] = [0] * 26
        window: List[int] = [0] * 26
        for i in range(len(s1)):
            target[ord(s1[i]) - ord("a")] += 1
        for i, c in enumerate(s2):
            window[ord(c) - ord("a")] += 1
            if i >= len(s1):
                window[ord(s2[i - len(s1)]) - ord("a")] -= 1
            if window == target:
                return True
        return False
