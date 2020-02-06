# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # first
        # for _ in range(0, k):
        #     nums.insert(0, nums.pop(len(nums) - 1))

        # second
        i = len(nums) - k
        nums[:] = nums[i:] + nums[:i]

        return nums
