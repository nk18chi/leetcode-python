# 944. Delete Columns to Make Sorted
# https://leetcode.com/problems/delete-columns-to-make-sorted/

from typing import List


class Solution:
    # O(n * m) in time, O(1) in space.
    def minDeletionSize(self, A: List[str]) -> int:
        count: int = 0
        for i in range(len(A[0])):
            for j in range(1, len(A)):
                if A[j - 1][i] > A[j][i]:
                    count += 1
                    break
        return count
