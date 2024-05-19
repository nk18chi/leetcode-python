# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    # This complexity can be more efficient, should be O(n)
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        dp: List[List[int]] = [
            [0 for _ in range(len(prices))] for _ in range(len(prices))
        ]
        for i in range(len(prices)):
            prevMax: int = dp[i - 2][i - 2] if i - 2 >= 0 and j - 2 >= 0 else 0
            for j in range(i, len(prices)):
                dp[i][j] = prices[j] - prices[i] + prevMax
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
