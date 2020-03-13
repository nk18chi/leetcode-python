# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

from typing import List, Dict, Set


class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     set: Set[int] = set()
    #     for n in nums:
    #         if n in set:
    #             return True
    #         set.add(n)
    #     return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
