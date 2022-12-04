# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution:
    # Brute Forcce
    # Time complexity: O(MN)
    # Space complexity: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack) - len(needle) + 1):
            isMatch: bool = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    isMatch = False
                    break
            if isMatch:
                return i
        return -1
