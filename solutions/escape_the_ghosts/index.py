# 789. Escape The Ghosts
# https://leetcode.com/problems/escape-the-ghosts/

from typing import List


class Solution:
    # def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
    #     minPath: float = float('inf')

    #     def dfs(row: int, col: int, count: int):
    #         if count > minPath:
    #             return -1
    #         if row == target[0] and col == target[1]:
    #             return count
    #         if row != target[0]:
    #             row += 1 if row < target[0] else - 1
    #             return dfs(row, col, count + 1)
    #         elif col != target[1]:
    #             col += 1 if col < target[1] else - 1
    #             return dfs(row, col, count + 1)

    #     minPath = dfs(0, 0, 0)
    #     for g in ghosts:
    #         if dfs(g[0], g[1], 0) > -1:
    #             return False
    #     return True

    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        minDist: int = abs(target[0]) + abs(target[1])
        for g in ghosts:
            if abs(target[0] - g[0]) + abs(target[1] - g[1]) <= minDist:
                return False
        return True
