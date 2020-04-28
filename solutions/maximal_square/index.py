# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/

from typing import List


class Solution:
    # Time complexity: O(m*n)
    # Space complexity: O(m*n)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        res: int = 0
        dp: List[List[int]] = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 if matrix[i - 1][j - 1] == "1" else 0
                res = max(res, dp[i][j])
        return res ** 2
