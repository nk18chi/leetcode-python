# 463. Island Perimeter
# https://leetcode.com/problems/island-perimeter/

from typing import List


class Solution:
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     if len(grid) < 0:
    #         return 0
    #     res: int = 0

    #     def dfs(row: int, col: int):
    #         if row < 0 or row >= len(grid):
    #             return 1
    #         if col < 0 or col >= len(grid[0]):
    #             return 1
    #         if grid[row][col] == 0:
    #             return 1
    #         if grid[row][col] == -1:
    #             return 0

    #         grid[row][col] = -1
    #         sum: int = 0
    #         sum += dfs(row - 1, col)
    #         sum += dfs(row, col + 1)
    #         sum += dfs(row + 1, col)
    #         sum += dfs(row, col - 1)

    #         return sum

    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == 1:
    #                 res = dfs(i, j)
    #                 return res

    #     return -1

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res: int = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if i == 0 or grid[i - 1][j] == 0:
                        res += 1
                    if i == len(grid) - 1 or grid[i + 1][j] == 0:
                        res += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        res += 1
                    if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                        res += 1
        return res
