# 896. Monotonic Array
# https://leetcode.com/problems/monotonic-array/

from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # # first solution
        # flag = 0
        # for i in range(len(A) - 1):
        #     if A[i] == A[i + 1]:
        #         continue

        #     if A[i] < A[i + 1]:
        #         if flag == -1:
        #             return False
        #         flag = 1
        #     elif A[i] > A[i + 1]:
        #         if flag == 1:
        #             return False
        #         flag = -1

        # return True

        # second solution
        isGreat = False
        isLess = False
        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                isGreat = True
            elif A[i - 1] > A[i]:
                isLess = True

            if isGreat and isLess:
                return False
        return True
