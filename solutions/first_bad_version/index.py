# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

from typing import Optional


answer: Optional[int] = None  # this value will be inserted in test.py


class Solution:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    def firstBadVersion(self, n) -> int:
        left: int = 1
        right: int = n
        while left <= right:
            mid: int = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


def isBadVersion(num: int):
    if answer is None:
        raise Exception()
    return num >= answer
