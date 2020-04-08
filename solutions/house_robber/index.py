# 198. House Robber
# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for n in nums:
            dp[0], dp[1] = dp[1], max(dp[1], dp[0] + n)
        return dp[1]
