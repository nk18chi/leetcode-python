# 344. Reverse String
# https://leetcode.com/problems/reverse-string/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reverseString(self, s: List[str]) -> None:
        left: int = 0
        right: int = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
