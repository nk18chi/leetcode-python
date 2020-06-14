# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List, Dict, Tuple, Deque
import collections
import heapq


class Solution:
    # Time complexity: O(v + e)
    # Space complexity: O(n)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        flightMap: Dict[int, List[List[int]]] = collections.defaultdict(list)
        for f in flights:
            flightMap[f[0]].append([f[1], f[2]])
        res: float = float("inf")
        q: Deque[List[int]] = collections.deque([[src, 0, K]])
        while len(q) > 0:
            cur: List[int] = q.popleft()  # (source, cost, k)
            for n, c in flightMap[cur[0]]:
                if n == dst:
                    res = min(res, c + cur[1])
                else:
                    if res >= c + cur[1] and cur[2] > 0:
                        q.append([n, c + cur[1], cur[2] - 1])
        return -1 if res == float("inf") else res

    # Time complexity: O((v + e)Logv)
    # Space complexity: O(n)
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    #     flightMap: Dict[int, List[Tuple[int, int]]] = collections.defaultdict(list)
    #     for s, d, cost in flights:
    #         flightMap[s].append((d, cost))
    #     heap: List[Tuple[int, int, int]] = [(0, src, K)]
    #     while len(heap) > 0:
    #         cur: Tuple[int, int, int] = heapq.heappop(heap)  # (cost, source, dest)
    #         if cur[1] == dst:
    #             return cur[0]
    #         if cur[2] < 0 or cur[1] not in flightMap:
    #             continue
    #         for n, c in flightMap[cur[1]]:
    #             heapq.heappush(heap, (cur[0] + c, n, cur[2] - 1))
    #     return -1
