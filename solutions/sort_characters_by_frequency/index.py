# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/

import heapq
from typing import List, Dict, Tuple


class Solution:
    # # sort solution
    # # Time complexity: O(nlogn)
    # # Space complexity: O(n)
    # def frequencySort(self, s: str) -> str:
    #     countMap: Dict[str, int] = {}
    #     for c in s:
    #         countMap[c] = countMap.get(c, 0) + 1
    #     sortedMap: List[Tuple[str, int]] = sorted(countMap.items(), key=lambda x: x[1], reverse=True)
    #     res: str = ""
    #     for sort in sortedMap:
    #         res += sort[0] * sort[1]
    #     return res

    # heap solution
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def frequencySort(self, s: str) -> str:
        countMap: Dict[str, int] = {}
        for c in s:
            countMap[c] = countMap.get(c, 0) + 1
        heap: List[int] = []
        for (key, value) in countMap.items():
            heapq.heappush(heap, (-value, key))
        res: str = ""
        while len(heap) > 0:
            h: Tuple[int, str] = heapq.heappop(heap)
            res += h[1] * -h[0]
        return res
