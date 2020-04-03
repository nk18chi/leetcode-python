# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # # first solution - O(n) in time, O(n) in space
        # insert is not O(1). https://wiki.python.org/moin/TimeComplexity
        # for _ in range(k):
        #     nums.insert(0, nums.pop())

        # second solution - O(n) in time, O(n) in space
        i = len(nums) - k
        nums[:] = nums[i:] + nums[:i]
