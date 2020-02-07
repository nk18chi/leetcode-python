# 704. Binary Search
# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    # helper
    def search(self, nums: List[int], target: int) -> int:
        def bs(self, list: List[int], start: int, end: int):
            if start > end:
                return -1
            mid: int = (end + start) // 2
            if list[mid] == target:
                return mid
            if list[mid] < target:
                return bs(self, list, mid + 1, end)
            else:
                return bs(self, list, start, mid - 1)
        return bs(self, nums, 0, len(nums) - 1)

    # # without helper
    # def search(self, nums: List[int], target: int) -> int:
    #     if len(nums) < 1:
    #         return -1
    #     mid: int = len(nums) // 2
    #     if nums[mid] == target:
    #         return mid
    #     if nums[mid] < target:
    #         val: int = self.search(nums[mid:], target)
    #         if
    #         return mid +
    #     else:
    #         return self.search(nums[mid:], target)
