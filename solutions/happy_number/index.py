# 202. Happy Number
# https://leetcode.com/problems/happy-number/

from typing import Set


class Solution:
    def isHappy(self, n: int) -> bool:
        check: Set[int] = set()
        while n not in check:
            check.add(n)
            nxt: int = 0
            while n > 0:
                nxt += (n % 10) ** 2
                n = n // 10
            n = nxt

        return n == 1
