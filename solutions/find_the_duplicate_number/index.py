# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        slow: int = nums[0]
        fast: int = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        n: int = 0
        while n != slow:
            n = nums[n]
            slow = nums[slow]
        return n
