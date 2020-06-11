# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/

from typing import List


class Solution:
    # Time xomplexity: O(n)
    # Space xomplexity: O(1)
    def sortColors(self, nums: List[int]) -> None:
        l: int = 0
        m: int = 0
        r: int = len(nums) - 1
        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            elif nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
