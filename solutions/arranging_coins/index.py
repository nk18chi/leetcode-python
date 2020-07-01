# 441. Arranging Coins
# https://leetcode.com/problems/arranging-coins/


class Solution:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    def arrangeCoins(self, n: int) -> int:
        left: int = 0
        right: int = n
        while left <= right:
            mid: int = (left + right) // 2
            cur: int = mid * (mid + 1) // 2
            if cur == n:
                return mid
            elif cur < n:
                left = mid + 1
            else:
                right = mid - 1
        return right
