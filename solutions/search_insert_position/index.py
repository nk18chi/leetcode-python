# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        while left <= right:
            mid: int = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
