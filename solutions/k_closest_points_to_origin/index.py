# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List, Tuple
import heapq


class Solution:
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    def kClosest(self, points, K):
        heap: List[Tuple(int, int, int)] = []
        for (a, b) in points:
            heapq.heappush(heap, (-(a ** 2 + b ** 2), a, b))
            if len(heap) > K:
                heapq.heappop(heap)
        return [[b, c] for (a, b, c) in heap]
