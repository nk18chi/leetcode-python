# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

from typing import List


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def longestPalindrome(self, s: str) -> str:
        index: List[int] = [0, 0]
        for i in range(len(s)):
            right: int = i + 1
            while right < len(s) and s[i] == s[right]:
                right += 1
            left: int = i - 1
            while 0 <= left and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            if index[1] - index[0] < right - left - 1:
                index[0] = left + 1
                index[1] = right
        return s[index[0] : index[1]]
