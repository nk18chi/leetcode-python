# 136. Single Number
# https://leetcode.com/problems/single-number/submissions/

from typing import List


class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     return sum(set(nums)) * 2 - sum(nums)

    def singleNumber(self, nums: List[int]) -> int:
        res: int = 0
        for n in nums:
            res ^= n
        return res
