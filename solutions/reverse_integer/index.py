# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/


class Solution:
    # Time complexity: O(1)
    # Space complexity: O(1)
    def reverse(self, x: int) -> int:
        sign: int = 1
        res: int = 0
        if x < 0:
            sign = -1
            x *= -1
        while x > 0:
            res = res * 10 + x % 10
            x //= 10
        return res * sign if res <= pow(2, 31) else 0
