# 78. Subsets
# https://leetcode.com/problems/subsets/

from typing import List


class Solution:
    # Time complexity: O(n^2**n)
    # Space complexity: O(n^2**n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = [[]]
        if len(nums) == 0:
            return res
        res.append([nums[0]])
        for n in nums[1:]:
            nxt: List[List[int]] = []
            for r in res:
                nxt.append(r + [n])
            res.extend(nxt)
        return res
