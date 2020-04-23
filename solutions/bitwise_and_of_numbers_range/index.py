# 201. Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/

import math


class Solution:
    # Time complexity: O(logn)^2 maybe..
    # Space complexity: O(1)
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res: int = 0
        while n > 0 and m > 0 and int(math.log(n, 2)) - int(math.log(m, 2)) == 0:
            i: int = pow(2, int(math.log(n, 2)))
            res += i
            n -= i
            m -= i
        return res
