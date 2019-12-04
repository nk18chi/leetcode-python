# 136. Single Number
# https://leetcode.com/problems/single-number/submissions/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)
