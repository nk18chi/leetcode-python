# 1. Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first solution
        # length = len(nums)
        # for i in range(0, length):
        #     if target <= i:
        #         continue

        #     for j in range(i + 1, length):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]

        # return []

        # second solution
        dict = {}

        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in dict:
                return [dict[remainder], index]
            else:
                dict[value] = index
