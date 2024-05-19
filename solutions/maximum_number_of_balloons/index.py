# 1189. Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/

from typing import Dict


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxNumberOfBalloons(self, text: str) -> int:
        charMap: Dict[str, int] = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for t in text:
            if t not in charMap:
                continue
            charMap[t] += 1
        charMap["l"] //= 2
        charMap["o"] //= 2
        return min(charMap.values())
