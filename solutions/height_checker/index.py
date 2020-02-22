# 1051. Height Checker
# https://leetcode.com/problems/height-checker/

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count: int = 0
        sortedHeights = sorted(heights)
        for a, b in zip(sortedHeights, heights):
            if a != b:
                count += 1
        return count
