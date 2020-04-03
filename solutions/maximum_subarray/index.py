# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr: List[int] = [nums[0], nums[0]]
        for n in nums[1:]:
            arr[1] = max(n, n + arr[1])
            arr[0] = max(arr[0], arr[1])
        return arr[0]
