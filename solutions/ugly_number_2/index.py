# 264. Ugly Number II
# https://leetcode.com/problems/ugly-number-ii/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Time complexity: O(n)
    def nthUglyNumber(self, n: int) -> int:
        ugly: List[int] = [1]
        i2: int = 0
        i3: int = 0
        i5: int = 0
        while n > 1:
            u2: int = 2 * ugly[i2]
            u3: int = 3 * ugly[i3]
            u5: int = 5 * ugly[i5]
            umin: int = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
