# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

from typing import Dict


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def firstUniqChar(self, s: str) -> int:
        countMap: Dict[str, int] = {}
        for c in s:
            countMap[c] = countMap.get(c, 0) + 1
        for i, c in enumerate(s):
            if countMap[c] == 1:
                return i
        return -1
