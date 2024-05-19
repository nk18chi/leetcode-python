# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix

from typing import List, Tuple


class Solution:
    # Time complexity: O(MN)
    # Space complexity: O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.res: List[int] = []

        def dfs(self, row: int, col: int, directionIndex: int):
            if (
                row < 0
                or row >= len(matrix)
                or col < 0
                or col >= len(matrix[row])
                or matrix[row][col] == 777
            ):
                return
            self.res.append(matrix[row][col])
            matrix[row][col] = 777

            nextRow: int = row + self.directions[directionIndex][0]
            nextCol: int = col + self.directions[directionIndex][1]
            if (
                nextRow < 0
                or nextRow >= len(matrix)
                or nextCol < 0
                or nextCol >= len(matrix[nextRow])
                or matrix[nextRow][nextCol] == 777
            ):
                directionIndex = (directionIndex + 1) % len(self.directions)
            nextRow = row + self.directions[directionIndex][0]
            nextCol = col + self.directions[directionIndex][1]
            dfs(self, nextRow, nextCol, directionIndex)

        dfs(self, 0, 0, 0)
        return self.res
