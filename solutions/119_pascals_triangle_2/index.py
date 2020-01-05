# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        res = [1, 1]
        i = 1
        while (i < rowIndex):
            list = [res[0]]
            for j in range(len(res) - 1):
                list += [res[j] + res[j + 1]]
            list += [res[-1]]
            res = list[::]
            i += 1

        return res
