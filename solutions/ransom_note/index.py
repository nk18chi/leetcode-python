# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/

from typing import Dict


class Solution:
    # Time complexity: O(m + n)
    # Space complexity: O(n)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charMap: Dict[str, int] = {}
        for m in magazine:
            charMap[m] = charMap.get(m, 0) + 1
        for r in ransomNote:
            if r not in charMap or charMap[r] < 1:
                return False
            charMap[r] -= 1
        return True
