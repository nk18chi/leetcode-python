# 581. Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

from typing import List


class Solution:
    # def findUnsortedSubarray(self, nums: List[int]) -> int:
    #     start: int = -1
    #     end: int = 0
    #     index: int = 0
    #     for origin, sort in zip(nums, sorted(nums)):
    #         if origin != sort:
    #             if start < 0:
    #                 start = index
    #             end = index
    #         index += 1
    #     return 0 if start < 0 else end - start + 1

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        sortedNums: List[int] = sorted(nums)
        lft, rgt = 0, len(nums) - 1
        while lft <= rgt and nums[lft] == sortedNums[lft]:
            lft += 1
        while lft <= rgt and nums[rgt] == sortedNums[rgt]:
            rgt -= 1
        return rgt - lft + 1
