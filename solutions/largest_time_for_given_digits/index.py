# 949. Largest Time for Given Digits - Easy
# https://leetcode.com/problems/largest-time-for-given-digits/

from typing import List, Set


class Solution:
    # def largestTimeFromDigits(self, A: List[int]) -> str:
    #     for first in [2, 1, 0]:
    #         a1List = A[:]
    #         if first in a1List:
    #             a1List.remove(first)
    #             second_range = range(
    #                 3, -1, -1) if first == 2 else range(9, -1, -1)
    #             for second in second_range:
    #                 a2List = a1List[:]
    #                 if second in a2List:
    #                     a2List.remove(second)
    #                     for third in range(5, -1, -1):
    #                         a3List = a2List[:]
    #                         if third in a3List:
    #                             a3List.remove(third)
    #                             return "%d%d:%d%d" % (
    #                                 first, second, third, a3List.pop())

    #     return ""

    # def largestTimeFromDigits(self, A: List[int]) -> str:
    #     patterns: List[int] = []

    #     def helper(res: int, checked: Set[int], n: int):
    #         for i in range(0, 4):
    #             if res > 2359 or res % 100 > 59:
    #                 return
    #             if n < 0:
    #                 patterns.append(res)
    #                 return
    #             if i in checked:
    #                 continue
    #             newSet = checked.copy()
    #             newSet.add(i)
    #             helper(res + A[i] * (10 ** n), newSet, n - 1)

    #     helper(0, set(), 3)
    #     if len(patterns) < 1:
    #         return ""
    #     patterns.sort(reverse=True)
    #     maxTime: str = str(patterns[0])
    #     if len(maxTime) < 4:
    #         zero: str = "0" * (4 - len(maxTime))
    #         maxTime = zero + maxTime
    #     return maxTime[:2] + ":" + maxTime[2:4]

    def largestTimeFromDigits(self, A: List[int]) -> str:
        import itertools

        res: int = -1
        for t in itertools.permutations(A):
            time: int = t[3] * 1000 + t[2] * 100 + t[1] * 10 + t[0]
            if time > 2359 or time % 100 > 59:
                continue
            res = max(res, time)

        return "" if res < 0 else "{:02d}:{:02d}".format(res // 100, res % 100)
