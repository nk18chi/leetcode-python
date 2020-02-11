# 693. Binary Number with Alternating Bits
# https://leetcode.com/problems/binary-number-with-alternating-bits/

# from typing import List, Dict


class Solution:
    # # first solution
    # def hasAlternatingBits(self, n: int) -> bool:
    #     binary: str = format(n, 'b')
    #     target: str = binary[0]
    #     for c in binary[1:]:
    #         if target == c:
    #             return False
    #         target = c
    #     return True

    # # second solution
    # def hasAlternatingBits(self, n: int) -> bool:
    #     target: int = n & 1
    #     n >>= 1
    #     while n:
    #         if target == n & 1:
    #             return False
    #         target = n & 1
    #         n >>= 1
    #     return True

    # third solution
    def hasAlternatingBits(self, n: int) -> bool:
        n = n ^ (n >> 1)
        return (n + 1) & n == 0
