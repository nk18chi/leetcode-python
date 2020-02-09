# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

from typing import List


# [
#     [0, 1, 1, 1]
#     [1, 2, 3, 4]
#     [1, 3, 6, 10]
#     [1, 4, 10, 20]
# ]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res: List[List[int]] = [[1 for x in range(m)] for y in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[-1][-1]

        # time limit exceed
        # def move(self, row, col):
        #     if row == m or col == n:
        #         self.count += 1
        #     else:
        #         move(self, row + 1, col)
        #         move(self, row, col + 1)

        # self.count = 0
        # move(self, 1, 1)
        # return self.count

        # second solution
        # aux = [[1 for x in range(n)] for x in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         aux[i][j] = aux[i][j - 1] + aux[i - 1][j]
        # return aux[-1][-1]
