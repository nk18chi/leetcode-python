# 504. Base 7
# https://leetcode.com/problems/base-7/submissions/


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res: str = ""
        n = abs(num)
        while n > 0:
            res = str(n % 7) + res
            n //= 7
        return "-" + res if num < 0 else res
