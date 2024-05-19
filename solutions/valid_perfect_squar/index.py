# 367. Valid Perfect Square - Easy
# https://leetcode.com/problems/valid-perfect-square/

# from typing import List


class Solution:
    # Binary Search Solution
    # Time complexity: O(logn)
    # Space complexity: O(1)
    def isPerfectSquare(self, num: int) -> bool:
        left: int = 0
        right: int = num
        while left <= right:
            mid: int = (left + right) // 2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
