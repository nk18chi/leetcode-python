# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/

from typing import List


class Solution:
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    def minDistance(self, word1: str, word2: str) -> int:
        dp: List[List[int]] = [
            [0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)
        ]
        for i in range(len(word1)):
            dp[i + 1][0] = i + 1
        for j in range(len(word2)):
            dp[0][j + 1] = j + 1
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
        return dp[-1][-1]
