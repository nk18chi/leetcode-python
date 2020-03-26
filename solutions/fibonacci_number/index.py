# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

from typing import List


class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        list: List[int] = [0, 1]
        i: int = 2
        while i < N:
            list[0], list[1] = list[1], sum(list)
            i += 1
        return sum(list)
