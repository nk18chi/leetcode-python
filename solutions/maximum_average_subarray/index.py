# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/

from typing import List

# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # # first solution
        # n = sum(nums[:k])
        # max_value = n
        # for f, s in zip(nums, nums[k:]):
        #     n += s
        #     n -= f
        #     max_value = max(max_value, n)
        # return max_value / k

        # second solution
        n = sum(nums[:k])
        max_value = n
        for i in range(k, len(nums)):
            n += nums[i] - nums[i - k]
            max_value = max(max_value, n)
        return max_value / k

        # time limit exceed
        # res = nums[::]
        # for i in range(len(nums[:-(k - 1)])):
        #     for j in range(i + 1, i + k):
        #         if j > len(nums):
        #             continue
        #         res[i] += nums[j]

        # return max(res) / k
