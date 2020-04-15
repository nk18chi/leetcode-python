# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left: int = 1
        right: int = 1
        res: List[int] = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            left *= nums[i - 1]
            right *= nums[-i]
            res[i] *= left
            res[-i - 1] *= right
        return res
