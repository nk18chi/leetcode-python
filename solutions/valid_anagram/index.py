# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

from typing import Dict
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap: Dict[str, int] = collections.defaultdict(int)
        for c in s:
            charMap[c] += 1
        for c in t:
            charMap[c] -= 1
        return all(v == 0 for v in charMap.values())
