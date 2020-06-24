# 137. Single Number II
# https://leetcode.com/problems/single-number-ii/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a: int = 0
        b: int = 0
        for n in nums:
            a = (a ^ n) & ~b
            b = (b ^ n) & ~a
        return a
