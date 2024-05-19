# 322. Coin Change
# https://leetcode.com/problems/coin-change/

from typing import List
import math


class Solution:
    # Time complexity: O(N * amount)
    # Space complexity: O(N)
    def coinChange(self, coins: List[int], amount: int) -> int:
        count: int = 0
        dp: List[float] = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        while count < amount:
            count += 1
            for coin in coins:
                if count - coin < 0:
                    continue
                dp[count] = min(dp[count - coin] + 1, dp[count])
        return -1 if math.isinf(dp[amount]) else int(dp[amount])
