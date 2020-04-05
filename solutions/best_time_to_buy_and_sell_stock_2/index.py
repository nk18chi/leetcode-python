# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List


class Solution:
    # O(n) in time, O(1) in space
    def maxProfit(self, prices: List[int]) -> int:
        res: int = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                res += prices[i] - prices[i - 1]
        return res
