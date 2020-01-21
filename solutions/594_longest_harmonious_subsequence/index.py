# 594. Longest Harmonious Subsequence
# https://leetcode.com/problems/longest-harmonious-subsequence/

from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict = {}
        for n in nums:
            dict[n] = dict.get(n, 0) + 1

        max_value = 0
        for k, v in dict.items():
            if k - 1 in dict:
                max_value = max(max_value, v + dict[k - 1])
        return max_value
