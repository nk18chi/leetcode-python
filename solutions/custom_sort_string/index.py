# 791. Custom Sort String
# https://leetcode.com/problems/custom-sort-string/

from typing import List, Dict


class Solution:
    # Time complexity: O(s + t + slogs)
    # Space complexity: O(2s) -> O(s)
    def customSortString(self, S: str, T: str) -> str:
        indexChar: Dict[str, List[int]] = {}
        for i, c in enumerate(S):
            indexChar[c] = [i, 0]
        res: str = ""
        for t in T:
            if t in indexChar:
                indexChar[t][1] += 1
            else:
                res += t
        sortedChar = sorted(indexChar.items(), key=lambda x: x[1])
        for k, v in sortedChar:
            res += k * v[1]
        return res
