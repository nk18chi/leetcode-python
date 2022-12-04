# 168. Excel Sheet Column Title - Easy
# https://leetcode.com/problems/excel-sheet-column-title/

# from typing import List


class Solution:
    # def convertToTitle(self, n: int) -> str:
    #     list = []
    #     while (0 < n):
    #         remainder = n % 26
    #         remainder = 26 if remainder == 0 else remainder
    #         list = [chr(ord("@") + remainder)] + list
    #         n -= remainder
    #         import math
    #         n = math.floor(n / 26)

    #     return "".join(list)

    def convertToTitle(self, columnNumber: int) -> str:
        res: str = ""
        while columnNumber > 0:
            columnNumber -= 1
            mod: int = columnNumber % 26
            res += chr(mod + 65)
            columnNumber //= 26
        return res[::-1]
