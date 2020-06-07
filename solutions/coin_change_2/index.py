# 518. Coin Change 2
# https://leetcode.com/problems/coin-change-2/

from typing import List


class Solution:
    # Time complexity: (mn), m is the length of coins
    # Space complexity: (n)
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[-1]
