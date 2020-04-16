# 139. Word Break
# https://leetcode.com/problems/word-break/

from typing import List


class Solution:
    # n is the length of "wordDict". m is the length of "s"
    # Time complexoty: O(n * m^2)
    # Space complexity: O(m)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp: List[bool] = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(len(s)):
            for w in wordDict:
                if dp[i - len(w) + 1] and s[i - len(w) + 1:i + 1] == w:
                    dp[i + 1] = True
        return dp[-1]
