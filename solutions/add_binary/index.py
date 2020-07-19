# 67. Add Binary
# https://leetcode.com/problems/add-binary/


class Solution:
    # Time complexity: O(1)
    # Space complexity: O(1)
    def addBinary(self, a: str, b: str) -> str:
        res: int = int(a, 2) + int(b, 2)
        return format(res, 'b')
