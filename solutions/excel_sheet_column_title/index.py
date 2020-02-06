# 168. Excel Sheet Column Title - Easy
# https://leetcode.com/problems/excel-sheet-column-title/

# from typing import List


class Solution:
    def convertToTitle(self, n: int) -> str:
        list = []
        while (0 < n):
            remainder = n % 26
            remainder = 26 if remainder == 0 else remainder
            list = [chr(ord("@") + remainder)] + list
            n -= remainder
            import math
            n = math.floor(n / 26)

        return "".join(list)
