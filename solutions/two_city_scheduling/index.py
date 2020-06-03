# 1029. Two City Scheduling
# https://leetcode.com/problems/two-city-scheduling/

import heapq
from typing import List, Tuple


class Solution:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        heap: List[Tuple[int, int, int]] = []
        for a, b in costs:
            heapq.heappush(heap, (a - b, a, b))
        res: int = 0
        for _ in range(len(costs) // 2):
            res += heapq.heappop(heap)[1]
        for _ in range(len(costs) // 2):
            res += heapq.heappop(heap)[2]
        return res
