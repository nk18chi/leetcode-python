# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List


class Solution:
    # # first solution(loop from top to target index)
    # def getRow(self, rowIndex: int) -> List[int]:
    #     res = [1]
    #     for i in range(1, rowIndex + 1):
    #         list = [0] * (i + 1)
    #         for j in range(i):
    #             list[j] += res[j]
    #             list[j + 1] += res[j]
    #         res = list[::]
    #     return res

    # second solution(math)
    def getRow(self, rowIndex: int) -> List[int]:
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(1, rowIndex + 1):
            res[i] = res[i - 1] * (rowIndex + 1 - i) // i
        return res

    # # previous solution
    # def getRow(self, rowIndex: int) -> List[int]:
    #     if rowIndex == 0:
    #         return [1]

    #     res = [1, 1]
    #     i = 1
    #     while (i < rowIndex):
    #         list = [res[0]]
    #         for j in range(len(res) - 1):
    #             list += [res[j] + res[j + 1]]
    #         list += [res[-1]]
    #         res = list[::]
    #         i += 1

    #     return res
