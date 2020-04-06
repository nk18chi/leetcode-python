# 944. Delete Columns to Make Sorted
# https://leetcode.com/problems/delete-columns-to-make-sorted/

from typing import List, Dict


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        check = 0
        for i in range(len(A[0])):
            stack = [ord(x[i]) for x in A]
            if stack != sorted(stack):
                check += 1

        return check

        # count: int = 0
        # for i in range(len(A[0])):
        #     for j in range(1, len(A)):
        #         if A[j - 1][i] > A[j][i]:
        #             count += 1
        #             break
        # return count
