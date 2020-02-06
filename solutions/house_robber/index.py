# 198. House Robber
# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for n in nums:
            dp[0], dp[1] = dp[1], max(dp[1], dp[0] + n)
        return dp[1]

    # # runtime error
    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]
    #     if len(nums) == 2:
    #         return max(nums[0], nums[1])
    #     if len(nums) == 3:
    #         return max(nums[0] + nums[2], nums[1])

    #     f = nums[0] + self.rob(nums[2:])
    #     s = nums[1] + self.rob(nums[3:])

    #     return max(f, s)
