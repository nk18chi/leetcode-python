# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List


class Solution:
    # # first solution(Time limit exceeded)
    # def maxProfit(self, prices: List[int]) -> int:
    #     if len(prices) < 2:
    #         return 0
    #     res: List[int] = [0] * len(prices)
    #     for i in range(1, len(prices)):
    #         p: List[int] = []
    #         for j in range(0, i):
    #             p.append(prices[i] - prices[j])
    #             if j > 0:
    #                 p[-1] += res[j - 1]
    #         res[i] = max(res[i - 1], max(p))
    #     return res[-1]

    # # second solution
    # def maxProfit(self, prices: List[int]) -> int:
    #     res: int = 0
    #     store: List[int] = [prices[0], prices[0]]
    #     for i in range(1, len(prices)):
    #         if prices[i - 1] > prices[i]:
    #             res += store[1] - store[0]
    #             store = [prices[i], prices[i]]
    #         else:
    #             store[1] = prices[i]
    #     res += store[1] - store[0]
    #     return res

    # third solution
    def maxProfit(self, prices: List[int]) -> int:
        res: int = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res
