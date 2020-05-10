# 997. Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/

from typing import List, Dict


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trustCount: Dict[int, int] = {}
        for (i, j) in trust:
            trustCount[i] = trustCount.get(i, 0) - 1
            trustCount[j] = trustCount.get(j, 0) + 1
        for (k, v) in trustCount.items():
            if v == N - 1:
                return k
        return -1 if N > 1 else 1
