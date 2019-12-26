# 1217. Play with Chips
# https://leetcode.com/problems/play-with-chips/

from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd_count = 0
        even_count = 0
        for c in chips:
            if c % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return min(odd_count, even_count)
