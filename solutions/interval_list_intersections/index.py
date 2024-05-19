# 986. Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/

from typing import List


class Solution:
    # Time complexity: O(m+n)
    # Space complexity: O(1)
    def intervalIntersection(
        self, A: List[List[int]], B: List[List[int]]
    ) -> List[List[int]]:
        a: int = 0
        b: int = 0
        res: List[List[int]] = []
        while a < len(A) and b < len(B):
            interval: List[int] = [max(A[a][0], B[b][0]), min(A[a][1], B[b][1])]
            if interval[0] <= interval[1]:
                res.append(interval)
            if A[a][1] < B[b][1]:
                a += 1
            elif A[a][1] > B[b][1]:
                b += 1
            else:
                a += 1
                b += 1
        return res
