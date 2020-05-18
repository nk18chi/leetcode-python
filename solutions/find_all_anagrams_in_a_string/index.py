# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pChar: List[int] = [0 for _ in range(26)]
        sChar: List[int] = [0 for _ in range(26)]
        for (pc, sc) in zip(p, s):
            pChar[ord(pc) - 97] += 1
            sChar[ord(sc) - 97] += 1
        res: List[int] = []
        index: int = 0
        while index <= len(s) - len(p):
            if sChar == pChar:
                res.append(index)
            if index + len(p) < len(s):
                sChar[ord(s[index]) - 97] -= 1
                sChar[ord(s[index + len(p)]) - 97] += 1
            index += 1
        return res
