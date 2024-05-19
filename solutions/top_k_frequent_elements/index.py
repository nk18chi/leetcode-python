# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from typing import List, Dict, Tuple


class Solution:
    # # Time complexity: O(nlogn)
    # # Space complexity: O(n)
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     countMap: Dict[int, int] = {}
    #     for n in nums:
    #         countMap[n] = countMap.get(n, 0) + 1
    #     sortedMap = sorted(countMap.items(), key=lambda x: x[1], reverse=True)
    #     return [x[0] for x in sortedMap][:k]

    # Time complexity: O(nlogk)
    # Space complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap: Dict[int, int] = {}
        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1
        heap: List[Tuple[int, int]] = []
        for key, value in countMap.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [h[1] for h in heap]
