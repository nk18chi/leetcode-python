# 949. Largest Time for Given Digits - Easy
# https://leetcode.com/problems/largest-time-for-given-digits/

from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        for first in [2, 1, 0]:
            a1List = A[:]
            if first in a1List:
                a1List.remove(first)
                second_range = range(
                    3, -1, -1) if first == 2 else range(9, -1, -1)
                for second in second_range:
                    a2List = a1List[:]
                    if second in a2List:
                        a2List.remove(second)
                        for third in range(5, -1, -1):
                            a3List = a2List[:]
                            if third in a3List:
                                a3List.remove(third)
                                return "%d%d:%d%d" % (
                                    first, second, third, a3List.pop())

        return ""
