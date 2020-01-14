# 1237. Find Positive Integer Solution for a Given Equation
# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

from typing import List

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""


class Solution:
    def findSolution(self,
                     customfunction,
                     z: int) -> List[List[int]]:
        # first solution
        list = []
        for i in range(1, 1001):
            for j in range(1, 1001):
                num = customfunction.f(i, j)
                if num == z:
                    list.append([i, j])
                if num > z:
                    break
        return list

        # second solution
        # list = []
        # for i in range(1, 1000):
        #     if customfunction.f(i, 1) > z:
        #         break
        #     for j in range(1, 1000):
        #         num = customfunction.f(i, j)
        #         if num == z:
        #             list.append([i, j])
        #         if num > z:
        #             break
        # return list

        # third solution
        # def bs(self, start, end, i):
        #     if start > end:
        #         return 0

        #     mid = (end + start) // 2
        #     num = customfunction.f(i, mid)
        #     if z == num:
        #         return mid
        #     elif z < num:
        #         return bs(self, start, mid - 1, i)
        #     else:
        #         return bs(self, mid +1, end, i)

        # list = []
        # for i in range(1, 1000):
        #     j = bs(self, 1, 1000, i)
        #     if j > 0:
        #         list.append([i, j])
        # return list
