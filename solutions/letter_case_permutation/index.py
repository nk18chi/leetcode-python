# 784. Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/

from typing import List

# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [""]
        for s in S:
            if s.isdecimal():
                for i in range(len(res)):
                    res[i] += s
            else:
                _s = s.lower() if s.isupper() else s.upper()
                length = len(res)
                for i in range(length):
                    res.append(res[i] + _s)
                    res[i] += s
        return res
