# 540. Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/

from typing import List


class Solution:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1
        while left < right:
            mid: int = (left + right) // 2
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
