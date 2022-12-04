# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    # Time complexity: O(logN)
    # Space complexity: O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res: List[int] = [-1, -1]
        left: int = 0
        right: int = len(nums) - 1
        if right < 0:
            return res

        while left < right:
            mid: int = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if nums[left] != target:
            return res
        else:
            res[0] = left

        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        res[1] = right
        return res
