# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

from typing import Set


class Solution:
    # Time complexity: (J + S)
    # Space complexity: (J)
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels: Set[str] = set(J)
        return sum(s in jewels for s in S)
