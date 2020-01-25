# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


class Solution:
    # # first solution
    # def findMin(self, nums: List[int]) -> int:
    #     def helper(self, start, end):
    #         if start > end:
    #             return - 1

    #         if start == end:
    #             return start - 1

    #         if end - start == 1:
    #             return start - 1 if nums[start] < nums[end] else start

    #         mid = (start + end) // 2
    #         if nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]:
    #             return mid - 1
    #         if nums[mid] < nums[end]:
    #             return helper(self, start, mid - 1)
    #         else:
    #             return helper(self, mid + 1, end)

    #     i = helper(self, 0, len(nums) - 1)
    #     return nums[i + 1]

    # second solution
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while (left < right):
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
