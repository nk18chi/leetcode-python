# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer: int = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[pointer], nums[i] = nums[i], nums[pointer]
            pointer += 1
