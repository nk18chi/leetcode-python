# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/

from typing import List


class Solution:
    # Time complexity: O(n*m)
    # Space complexity: O(n*m)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp: List[List[int]] = [
            [0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)
        ]
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
