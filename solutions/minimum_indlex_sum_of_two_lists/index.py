# 599. Minimum Index Sum of Two Lists
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

from typing import List, Dict


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        interests: Dict[str, int] = {}
        for i, r in enumerate(list1):
            interests[r] = i

        res: List[str] = []
        minSum: float = float('inf')
        for i, r in enumerate(list2):
            if r not in interests:
                continue
            if interests[r] + i < minSum:
                res = [r]
                minSum = interests[r] + i
            elif interests[r] + i == minSum:
                res.append(r)

        return res
