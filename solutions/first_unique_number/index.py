# First Unique Number
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3313/

from typing import List, Dict


class Solution:
    # Space complexity: O(n)
    class FirstUnique:
        def __init__(self, nums: List[int]):
            self.queue: List[int] = nums
            self.countMap: Dict[int, int] = {}
            for n in nums:
                self.countMap[n] = self.countMap.get(n, 0) + 1
            self.index = 0

        # Time complexity: O(n)
        def showFirstUnique(self) -> int:
            while self.index < len(self.queue):
                if self.countMap[self.queue[self.index]] < 2:
                    return self.queue[self.index]
                self.index += 1
            return -1

        # Time complexity: O(1)
        def add(self, value: int) -> None:
            self.queue.append(value)
            self.countMap[value] = self.countMap.get(value, 0) + 1
