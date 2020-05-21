# 1277. Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

from typing import List


class Solution:
    # Time complexity: O(mn)
    # Space complexity: O(1)
    def countSquares(self, matrix: List[List[int]]) -> int:
        res: int = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    continue
                if r > 0 and c > 0:
                    matrix[r][c] += min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])
                res += matrix[r][c]
        return res
