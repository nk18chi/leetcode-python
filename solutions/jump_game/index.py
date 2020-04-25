# 55. Jump Game
# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    # # DP solution by bottom-up
    # # Time complexity: O(n^2)
    # # Space complexity: O(n)
    # def canJump(self, nums: List[int]) -> bool:
    #     check: List[int] = [0 for _ in range(len(nums))]
    #     check[-1] = 1
    #     for i in range(len(nums) - 2, -1, -1):
    #         total: int = sum(check[i:]) if nums[i] + i > len(nums) - 1 else sum(check[i: nums[i] + i + 1])
    #         check[i] = 1 if total > 0 else 0
    #     return check[0] == 1

    # Greedy
    # Time complexity: O(n)
    # Space complexity: O(1)
    def canJump(self, nums: List[int]) -> bool:
        lastIndex: int = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= lastIndex:
                lastIndex = i
        return lastIndex == 0
