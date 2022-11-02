# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/

class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def mySqrt(self, x: int) -> int:
        left: int = 0
        right: int = x
        while left <= right:
            mid: int = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif x < mid * mid:
                right = mid - 1
            else:
                return mid
        return right
