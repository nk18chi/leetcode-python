# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        list = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    list[i] = max(list[i], list[j] + 1)
        return max(list)
