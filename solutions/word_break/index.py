# 139. Word Break
# https://leetcode.com/problems/word-break/

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        checked: List[int] = [False for _ in range(len(s))]

        def helper(s: str, wordDict: List[str]) -> bool:
            if len(s) == 0:
                return True
            if checked[len(s) - 1]:
                return False
            res: bool = False
            for word in wordDict:
                length: int = len(word)
                if s[:length] == word:
                    res = helper(s[length:], wordDict)
                    if res:
                        return res
            checked[len(s) - 1] = True
            return False

        return helper(s, wordDict)
