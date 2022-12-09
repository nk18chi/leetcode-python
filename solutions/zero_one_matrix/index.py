# 542. 01 Matrix
# https://leetcode.com/problems/01-matrix/description/

from typing import List, Deque, Tuple
from collections import deque


class Solution:
    # Time complexity: O(MN)
    # Space complexity: O(MN)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res: List[List[int]] = [[-1 for _ in range(len(mat[i]))] for i in range(len(mat))]
        queue: Deque[Tuple[int, int]] = deque([])
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    res[i][j] = 0
        while len(queue) > 0:
            q: Tuple[int, int] = queue.popleft()
            for pos in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                row: int = q[0] + pos[0]
                col: int = q[1] + pos[1]
                if row < 0 or row >= len(mat):
                    continue
                if col < 0 or col >= len(mat[row]):
                    continue
                if res[row][col] > -1:
                    continue
                res[row][col] = res[q[0]][q[1]] + 1
                queue.append((row, col))
        return res
