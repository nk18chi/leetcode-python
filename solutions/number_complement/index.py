# 476. Number Complement
# https://leetcode.com/problems/number-complement/

import math


class Solution:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    def findComplement(self, num: int) -> int:
        return pow(2, math.floor(math.log(num, 2)) + 1) - 1 ^ num
