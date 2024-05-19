# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxArea(self, height: List[int]) -> int:
        res: int = 0
        left: int = 0
        right: int = len(height) - 1
        while left < right:
            square: int = min(height[left], height[right]) * (right - left)
            res = max(res, square)
            if height[left] == height[right]:
                left += 1
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
