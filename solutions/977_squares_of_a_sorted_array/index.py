# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # first solution
        # list = []
        # for a in A:
        #     list.append(a * a)
        # list.sort()
        # return list

        # second solution
        length = len(A)
        res = [0] * length
        left, right = 0, length - 1
        for i in range(length - 1, -1, -1):
            lft = A[left] ** 2
            rgt = A[right] ** 2
            if (lft < rgt):
                res[i] = rgt
                right -= 1
            else:
                res[i] = lft
                left += 1
        return res
