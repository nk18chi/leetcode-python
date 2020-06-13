# 368. Largest Divisible Subset
# https://leetcode.com/problems/largest-divisible-subset/

from typing import List


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        nums.sort()
        dp: List[List[int]] = [[n] for n in nums]
        res: List[int] = [nums[0]]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
            if len(res) < len(dp[i]):
                res = dp[i]
        return res
