# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res: int = 0

        def dfs(row: int, col: int):
            if row < 0 or row > len(grid) - 1:
                return
            if col < 0 or col > len(grid[0]) - 1:
                return
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res
