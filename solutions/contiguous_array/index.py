# 525. Contiguous Array
# https://leetcode.com/problems/contiguous-array/

from typing import List, Dict


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def findMaxLength(self, nums: List[int]) -> int:
        indexMap: Dict[int, int] = {0: -1}
        count: int = 0
        maxLength: int = 0
        for i, n in enumerate(nums):
            count += 1 if n == 1 else -1
            if count in indexMap:
                maxLength = max(maxLength, i - indexMap[count])
            else:
                indexMap[count] = i
        return maxLength

    # Brute force - Time Limit Exceeded
    # # Time complexity: O(n^2)
    # # Space complexity: O(n)
    # def findMaxLength(self, nums: List[int]) -> int:
    #     prev: List[List[int]] = []
    #     maxLength: int = 0
    #     for n in nums:
    #         for p in prev:
    #             if n == 0:
    #                 p[0] += 1
    #             else:
    #                 p[1] += 1
    #             if p[0] == p[1] and maxLength < p[0] * 2:
    #                 maxLength = p[0] * 2
    #         if n == 0:
    #             prev.append([1, 0])
    #         else:
    #             prev.append([0, 1])

    #     return maxLength
