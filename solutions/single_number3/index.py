# 260. Single Number III
# https://leetcode.com/problems/single-number-iii/

from typing import List, Dict


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def singleNumber(self, nums: List[int]) -> List[int]:
        countMap: Dict[int, int] = {}
        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1
        res: List[int] = []
        for k, v in countMap.items():
            if v > 1:
                continue
            res.append(k)
        return res
