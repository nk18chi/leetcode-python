# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    # # first solution(recursion, time limit exceeded)
    # def maxProfit(self, prices: List[int]) -> int:
    #     if len(prices) < 2:
    #         return 0
    #     self.min: int = prices[0] + 1
    #     self.diff: int = 0

    #     def helper(self, prices) -> None:
    #         if len(prices) < 2:
    #             return
    #         if self.min <= prices[0]:
    #             helper(self, prices[1:])
    #             return
    #         self.min = prices[0]

    #         for i in range(1, len(prices)):
    #             self.diff = max(self.diff, prices[i] - prices[0])
    #         helper(self, prices[1:])
    #     helper(self, prices)
    #     return self.diff

    # # second solution(recursion, time limit exceeded)
    # def maxProfit(self, prices: List[int]) -> int:
    #     diff: List[int] = [0] * len(prices)
    #     for i in range(1, len(prices)):
    #         for j in range(i):
    #             diff[j] = max(diff[j], prices[i] - prices[j])
    #     return max(diff)

    # third solution(dynamic programing)
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp: List[int] = [0, prices[0]]
        for i in range(1, len(prices)):
            dp[0] = max(dp[0], prices[i] - dp[1])
            dp[1] = min(dp[1], prices[i])
        return dp[0]
