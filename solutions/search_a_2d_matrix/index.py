# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    # Time Complexity O(log(mn))
    # Space Complexity O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left: int = 0
        right: int = len(matrix) - 1
        while left <= right:
            mid: int = (right + left) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        targetRow = left - 1
        if(targetRow < 0):
            return False
        left = 0
        right = len(matrix[targetRow]) - 1
        while left <= right:
            mid = (right + left) // 2
            if matrix[targetRow][mid] == target:
                return True
            elif matrix[targetRow][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
