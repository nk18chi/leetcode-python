# 1200. Minimum Absolute Difference
# https://leetcode.com/problems/minimum-absolute-difference/

from typing import List


class Solution:
    # # first solution
    # def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    #     arr.sort()
    #     dict = {}
    #     for i in range(len(arr) - 1):
    #         diff = arr[i + 1] - arr[i]
    #         if diff not in dict:
    #             dict[diff] = []
    #         dict[diff].append([arr[i], arr[i + 1]])

    #     _min = min(dict.keys())
    #     return dict[_min]

    # second solution
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        _min = float("inf")
        res = []
        for i in range(len(arr) - 1):
            abs = arr[i + 1] - arr[i]
            if abs > _min:
                continue

            if abs < _min:
                res = []
                _min = abs
            res.append([arr[i], arr[i + 1]])
        return res
