# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List, Dict
import collections


class Solution:
    # Time complexity: O(M+N)
    # Space complexity: O(min(M, N))
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count: Dict[int, int] = collections.defaultdict(int)
        res: List[int] = []
        for n in nums1:
            count[n] += 1
        for n in nums2:
            if count[n] > 0:
                res.append(n)
                count[n] -= 1
        return res
