# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import Dict


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        res: int = 0
        start: int = -1
        map: Dict[str, int] = {}
        for i in range(len(s)):
            if s[i] in map:
                start = max(start, map[s[i]])
                res = max(res, i - start)
            else:
                res = max(res, i - start)
            map[s[i]] = i
        return res
