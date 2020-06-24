# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/

from typing import List


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def numTrees(self, n: int) -> int:
        dp: List[int] = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]
