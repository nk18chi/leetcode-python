from typing import List, Set, Dict, Tuple, Deque
from collections import deque, defaultdict
from _class.tree_node import TreeNode


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count: int = 0
        for a in arr:
            if a % 2 == 0:
                count = 0
            else:
                count += 1
                if count == 3:
                    return True
        return False

    def minOperations(self, n: int) -> int:
        count: int = 0
        for i in range(n // 2):
            count += n - ((2 * i) + 1)
        return count

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans

        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l
