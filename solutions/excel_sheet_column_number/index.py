# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def titleToNumber(self, columnTitle: str) -> int:
        res: int = 0
        n: int = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            res += (ord(columnTitle[i]) - 64) * pow(26, n)
            n += 1
        return res
