# 268. Missing Number
# https://leetcode.com/problems/missing-number/submissions/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sort, Time complexity: O(nlogn), Space complexity: O(1)
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return len(nums)

        # Sum, Time complexity: O(n), Space complexity: O(1)
        # n: int = len(nums)
        # return (n * (n + 1)) // 2 - sum(nums)

        # XOR, Time complexity: O(n), Space complexity: O(1)
        n: int = len(nums)
        for i in range(len(nums)):
            n ^= i
            n ^= nums[i]
        return n
