# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/description/

from typing import List, Tuple, Deque
from collections import deque


class Solution:
    # Time complexity: O(MN)
    # Space complexity: O(MN)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total: int = 0
        rotten: int = 0
        stack: Deque[Tuple[int, int]] = deque([])
        minutes: int = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    total += 1
                if grid[i][j] == 2:
                    stack.append((i, j))
                    rotten += 1
                    total += 1
        while stack and total > rotten:
            for _ in range(len(stack)):
                pop: Tuple[int, int] = stack.popleft()
                for p in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    row: int = pop[0] + p[0]
                    col: int = pop[1] + p[1]
                    if row < 0 or row >= len(grid):
                        continue
                    if col < 0 or col >= len(grid[row]):
                        continue
                    if grid[row][col] != 1:
                        continue
                    rotten += 1
                    grid[row][col] = 2
                    stack.append((row, col))
            minutes += 1
        return minutes if total == rotten else -1
