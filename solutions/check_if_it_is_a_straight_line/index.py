# 1232. Check If It Is a Straight Line
# https://leetcode.com/problems/check-if-it-is-a-straight-line/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xDiff1: int = coordinates[1][0] - coordinates[0][0]
        yDiff1: int = coordinates[1][1] - coordinates[0][1]
        for i in range(2, len(coordinates)):
            xDiff2: int = coordinates[i][0] - coordinates[i - 1][0]
            yDiff2: int = coordinates[i][1] - coordinates[i - 1][1]
            if xDiff1 * yDiff2 != xDiff2 * yDiff1:
                return False
        return True
