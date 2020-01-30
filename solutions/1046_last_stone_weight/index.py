# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/

from typing import List


class Solution:
    # first solution
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            if stones[0] == stones[1]:
                del stones[1]
                del stones[0]
            else:
                stones[0] = stones[0] - stones[1]
                del stones[1]
        return stones[0] if len(stones) == 1 else 0

        # # second solution
        # while len(stones) > 1:
        #     _max = max(stones)
        #     stones.remove(_max)
        #     _max_second = max(stones)
        #     stones.remove(_max_second)
        #     if _max != _max_second:
        #         stones.append(_max - _max_second)
        # return stones[0] if len(stones) == 1 else 0

        # # Priority Queue1
        # import heapq
        # h = [-x for x in stones]
        # heapq.heapify(h)
        # while len(h) > 1 and h[0] != 0:
        #     heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        # return -h[0]

        # # Priority Queue2
        # import bisect
        # stones.sort()
        # while len(stones) > 1:
        #     bisect.insort(stones, stones.pop() - stones.pop())
        # return stones[0]
