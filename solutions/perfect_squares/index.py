# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/

from typing import List


class Solution:
    # Time complexiy: O(n * rootn)
    # Space complexiy: O(n + rootn)
    def numSquares(self, n: int) -> int:
        dp: List[int] = [0 for _ in range(n + 1)]
        choices: List[int] = []
        i: int = 1
        j: int = 1
        while i <= n:
            if j * j == i:
                choices.append(j * j)
                j += 1
            res: float = float("inf")
            for c in choices:
                res = min(res, dp[i - c])
            dp[i] = int(res)
            i += 1
        return dp[-1]
