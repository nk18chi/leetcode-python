# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    # Time complexity: O(S) S is the sum of all letters in given words
    # Space complexity: O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            cur: str = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != cur:
                    return word[:i]
        return strs[0]
