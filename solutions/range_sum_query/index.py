# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List


class Solution:
    class NumArray:
        # def __init__(self, nums: List[int]):
        #     self.nums: List[int] = nums

        # def sumRange(self, i: int, j: int) -> int:
        #     return sum(self.nums[i:j + 1])

        def __init__(self, nums: List[int]):
            self.nums = []
            if len(nums) < 1:
                return
            self.nums.append(nums[0])
            for i in range(1, len(nums)):
                self.nums.append(self.nums[i - 1] + nums[i])

        def sumRange(self, i: int, j: int) -> int:
            if i == 0:
                return self.nums[j] - 0
            return self.nums[j] - self.nums[i - 1]
