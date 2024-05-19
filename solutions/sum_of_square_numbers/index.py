# 633. Sum of Square Numbers
# https://leetcode.com/problems/sum-of-square-numbers/

# from typing import List


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math

        for i in range(int(math.sqrt(c)) + 1):
            if math.sqrt(c - i**2).is_integer():
                return True
        return False
