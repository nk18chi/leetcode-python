# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/

from typing import List


class Solution:
    # sort solution
    # Time complexity: O(n^2logn)
    # Space complexity: O(1)
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            max1: int = stones.pop()
            max2: int = stones.pop()
            if max1 > max2:
                stones.append(max1 - max2)
        return stones[0] if len(stones) == 1 else 0

    # # priority queue solution1 by @lee215
    # # Time complexity: O(nlogn)
    # # Space complexity: O(n)
    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     import heapq
    #     h = [-x for x in stones]
    #     heapq.heapify(h)
    #     while len(h) > 1 and h[0] != 0:
    #         heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
    #     return -h[0]

    # # priority queue solution2 by @lee215
    # # Time complexiy: O(n^2)
    # # Space complexiy: O(1)
    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     import bisect
    #     stones.sort()
    #     while len(stones) > 1:
    #         bisect.insort(stones, stones.pop() - stones.pop())
    #     return stones[0]
