# 1254. Number of Closed Islands
# https://leetcode.com/problems/number-of-closed-islands/

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        res: int = 0

        def dfs(row: int, col: int) -> bool:
            if row < 0 or row > len(grid) - 1:
                return False
            if col < 0 or col > len(grid[0]) - 1:
                return False
            if grid[row][col] > 0:
                return True
            grid[row][col] = 2
            top: bool = dfs(row - 1, col)
            right: bool = dfs(row, col + 1)
            bottom: bool = dfs(row + 1, col)
            left: bool = dfs(row, col - 1)
            return top and right and bottom and left

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                if grid[i][j] == 0:
                    res += 1 if dfs(i, j) else 0
        return res
