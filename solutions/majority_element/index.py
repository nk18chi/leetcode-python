# 169. Majority Element
# https://leetcode.com/problems/majority-element/

from typing import List, Dict


class Solution:
    # # Time complexity: O(n)
    # # Space complexity: O(n)
    # def majorityElement(self, nums: List[int]) -> int:
    #     countMap: Dict[int, int] = {}
    #     for n in nums:
    #         countMap[n] = countMap.get(n, 0) + 1
    #     for (key, value) in countMap.items():
    #         if value > len(nums) // 2:
    #             return key
    #     return -1

    # Time complexity: O(n)
    # Space complexity: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        count: int = 0
        cur: int = 0
        for n in nums:
            if count == 0:
                cur = n
            count += 1 if cur == n else -1
        return cur
