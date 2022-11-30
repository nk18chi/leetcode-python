# 326. Power of Three
# https://leetcode.com/problems/power-of-three/submissions/


class Solution:
    # Time complexity: O(log3 n)
    # Space complexity: O(1)
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
