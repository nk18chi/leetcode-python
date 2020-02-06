# 412. Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res: List[str] = [""] * n
        for i in range(1, n + 1):
            if i % 3 == 0:
                res[i - 1] += "Fizz"
            if i % 5 == 0:
                res[i - 1] += "Buzz"
            if not res[i - 1]:
                res[i - 1] = str(i)

        return res
