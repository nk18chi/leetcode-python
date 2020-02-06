# 409. Longest Palindrome - Easy
# https://leetcode.com/problems/longest-palindrome/

# from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

        total = 0
        for count in dict.values():
            if count % 2 == 0:
                total += count
            elif count > 2:
                total += count - 1

        if total != len(s):
            total += 1

        return total
