# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def countBits(self, num: int) -> List[int]:
        res: List[int] = [0]
        while len(res) <= num:
            res += [res[x] + 1 for x in range(len(res))]
        return res[: num + 1]
