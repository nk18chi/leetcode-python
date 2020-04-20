# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        def bs(start: int, end: int):
            if start > end:
                return -1
            mid: int = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] <= target < nums[mid]:
                return bs(start, mid - 1)
            elif nums[mid] < target <= nums[end]:
                return bs(mid + 1, end)

            if nums[start] > nums[mid]:
                return bs(start, mid - 1)
            else:
                return bs(mid + 1, end)
        return bs(0, len(nums) - 1)
