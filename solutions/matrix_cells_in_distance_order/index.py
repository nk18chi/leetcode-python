# 1030. Matrix Cells in Distance Order
# https://leetcode.com/problems/matrix-cells-in-distance-order/

from typing import List

# Input: R = 1, C = 2, r0 = 0, c0 = 0
# Output: [[0,0],[0,1]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1]


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # first solution
        # res, order = [], []
        # for r in range(R):
        #     for c in range(C):
        #         res += [[r, c]]
        #         order += [abs(r - r0) + abs(c - c0)]
        # order, res = zip(*sorted(zip(order, res)))
        # return list(res)

        # second solution
        # def dfs(self, row, col):
        #     if row < 0 or row >= R or col < 0 or col >= C:
        #         return

        #     if (row, col) in checked:
        #         return
        #     checked.add((row, col))

        #     distance = abs(row - r0) + abs(col - c0)
        #     if distance in dict:
        #         dict[distance] += [[row, col]]
        #     else:
        #         dict[distance] = [[row, col]]

        #     dfs(self, row + 1, col)
        #     dfs(self, row - 1, col)
        #     dfs(self, row, col + 1)
        #     dfs(self, row, col - 1)

        # dict, checked = {}, set()
        # dfs(self, r0, c0)
        # result = []
        # for n in range(max(dict.keys()) + 1):
        #     result += dict[n]

        # return result

        # third solution
        res = []
        for r in range(R):
            for c in range(C):
                res += [[r, c]]

        return sorted(res, key=lambda l: abs(r0 - l[0]) + abs(c0 - l[1]))
