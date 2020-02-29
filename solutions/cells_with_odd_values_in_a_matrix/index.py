# 1252. Cells with Odd Values in a Matrix
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

from typing import List


class Solution:
    # Time Comprexity: (m + n) * l(indices.count) + m * n
    # Space Comprexity: m * n

    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix: List[List[int]] = [[0 for _ in range(m)] for _ in range(n)]
        for indice in indices:
            row: int = indice[0]
            col: int = indice[1]
            for i in range(m):
                matrix[row][i] += 1
            for i in range(n):
                matrix[i][col] += 1

        count: int = 0
        for arr in matrix:
            for n in arr:
                if n % 2 == 1:
                    count += 1
        return count
