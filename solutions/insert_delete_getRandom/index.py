# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random
from typing import List, Dict


class Solution:
    # Time complexity: O(1)
    # Space complexity: O(n)
    class RandomizedSet:
        def __init__(self):
            self.posMap: Dict[int, int] = {}
            self.nums: List[int] = []

        def insert(self, val: int) -> bool:
            if val in self.posMap:
                return False
            self.nums.append(val)
            self.posMap[val] = len(self.nums) - 1
            return True

        def remove(self, val: int) -> bool:
            if len(self.nums) == 0 or val not in self.posMap:
                return False
            idx: int = self.posMap[val]
            last: int = self.nums[-1]
            self.nums[idx] = last
            self.nums.pop()
            self.posMap[last] = idx
            del self.posMap[val]
            return True

        def getRandom(self) -> int:
            return random.choice(self.nums)
