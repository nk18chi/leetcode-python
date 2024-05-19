# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        left: int = 0
        right: int = 1
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1
        nums = nums[: left + 1]
        return left + 1
