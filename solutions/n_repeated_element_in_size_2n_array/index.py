# 961. N-Repeated Element in Size 2N Array
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

from typing import List, Dict


class Solution:
    # # first solution
    # def repeatedNTimes(self, A: List[int]) -> int:
    #     length: int = len(A)
    #     dict: Dict[int, int] = {}
    #     for a in A:
    #         dict[a] = dict.get(a, 0) + 1
    #         if dict[a] == length // 2:
    #             return a
    #     return - 1

    # second solution
    def repeatedNTimes(self, A: List[int]) -> int:
        dict: Dict[int, int] = {}
        for a in A:
            dict[a] = dict.get(a, 0) + 1
            if dict[a] > 1:
                return a
        return -1

    # # Third solution
    # def repeatedNTimes(self, A: List[int]) -> int:
    #     times: int = len(A) // 2 - 1
    #     diff = sum(A) - sum(set(A))
    #     return diff // times
