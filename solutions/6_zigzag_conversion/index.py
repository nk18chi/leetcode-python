# 6. ZigZag Conversion
# https://leetcode.com/problems/zigzag-conversion/

# Input: s = "PAYPALISHIRING", numRows = 3
# P   A   H   N
# A P L S I I G
# Y   I   R
# Output: "PAHNAPLSIIGYIR"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = [""] * numRows
        index = 0
        isDiagonal = False
        for c in s:
            res[index] += c
            index = index - 1 if isDiagonal else index + 1
            if index == numRows - 1:
                isDiagonal = True
            if index == 0:
                isDiagonal = False

        return "".join(res)
