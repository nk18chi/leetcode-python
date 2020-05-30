# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List, Tuple
import heapq


class Solution:
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    def kClosest(self, points, K):
        heap: List[Tuple[int, List[int]]] = []
        for p in points:
            heapq.heappush(heap, [-(p[0] ** 2 + p[1] ** 2), p])
            if len(heap) > K:
                heapq.heappop(heap)
        return [h[1] for h in heap]
