# 1154. Day of the Year
# https://leetcode.com/problems/day-of-the-year/

# from typing import List


class Solution:
    def dayOfYear(self, date: str) -> int:
        month_days = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        Y, M, D = map(int, date.split("-"))

        if Y % 4 == 0 and Y % 100 != 0:
            month_days[2] += 1

        days = 0
        for i in range(1, M):
            days += month_days[i]
        days += int(D)

        return days
