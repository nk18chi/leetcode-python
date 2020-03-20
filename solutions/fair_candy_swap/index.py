# 888. Fair Candy Swap
# https://leetcode.com/problems/fair-candy-swap/

from typing import List, Set


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        setA: Set[int] = set(A)
        setB: Set[int] = set(B)
        sumA = sum(A)
        sumB = sum(B)
        half: int = (sumA + sumB) // 2
        for n in setA:
            x: int = half - sumA + n
            if x in setB:
                return [n, x]
        return []
