# 528. Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/

import random
from typing import List


class Solution:
    # Space complexity: O(n)
    def __init__(self, w: List[int]):
        self.w: List[int] = [w[0]]
        for n in w[1:]:
            self.w.append(n + self.w[-1])

    # Time complexity: O(log)
    # Space complexity: O(1)
    def pickIndex(self) -> int:
        target: int = random.randint(1, self.w[-1])
        left: int = 0
        right: int = len(self.w) - 1
        while left < right:
            mid: int = (left + right) // 2
            if self.w[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
