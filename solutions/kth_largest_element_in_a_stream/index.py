# 703. Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from typing import List
import heapq


class Solution:
    class KthLargest:
        # Time complexity: O(nlogk)
        # Space complexity: O(1), technically O(k)
        def __init__(self, k: int, nums: List[int]):
            self.heap: List[int] = []
            self.k = k
            for n in nums:
                self.add(n)

        # Time complexity: O(logk)
        def add(self, val: int) -> int:
            if len(self.heap) == self.k:
                if self.heap[0] >= val:
                    return self.heap[0]
                heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
            return self.heap[0]
