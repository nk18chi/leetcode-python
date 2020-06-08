# 231. Power of Two - Easy
# https://leetcode.com/problems/power-of-two/


class Solution:
    # Time complexity: O(1)
    # Space complexity: O(1)
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
