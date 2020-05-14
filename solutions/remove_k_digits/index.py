# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/

# from typing import List, Dict


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        self.res: float = float("inf")

        def helper(num: str, k: int, cur: str):
            if k == 0:
                self.res = min(self.res, int(cur + num))
                return
            if len(num) < k:
                return
            helper(num[1:], k - 1, cur)
            helper(num[1:], k, cur + num[0])
        helper(num, k, "0")
        return str(self.res)
