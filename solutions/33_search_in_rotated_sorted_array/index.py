# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length < 1:
            return - 1
        elif length == 1:
            return 0 if nums[0] == target else - 1
        elif length == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        result = self.getRotatedPointByBnarySearch(nums, 0, len(nums) - 1)
        index = 0
        if result == -1:
            nums = nums
        elif nums[0] <= target <= nums[result]:
            nums = nums[0:result + 1]
        elif nums[result + 1] <= target <= nums[length - 1]:
            index = result + 1
            nums = nums[index:]
        else:
            return -1

        result = self.binarySearch(target, nums, 0, len(nums) - 1)
        if result < 0:
            return result
        return index + result

    def getRotatedPointByBnarySearch(self, nums, start, end):
        if len(nums) <= 0:
            return -1
        elif len(nums) == 1:
            return 0
        else:
            import math
            mid = math.floor((start + end) / 2)
            if nums[mid] < nums[start]:
                return self.getRotatedPointByBnarySearch(nums, start, mid)
            elif nums[end] < nums[mid]:
                return self.getRotatedPointByBnarySearch(nums, mid + 1, end)
            else:
                return start - 1

    def binarySearch(self, i, nums, start, end):
        if start == end:
            if nums[start] == i:
                return start
            else:
                return -1
        else:
            import math
            mid = math.floor((start + end) / 2)
            if i == nums[mid]:
                return mid
            elif i < nums[mid]:
                return self.binarySearch(i, nums, start, mid)
            else:
                return self.binarySearch(i, nums, mid + 1, end)
