# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

from typing import List


class Solution:
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    def uniquePaths(self, m: int, n: int) -> int:
        dp: List[List[int]] = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[-1][-1]
