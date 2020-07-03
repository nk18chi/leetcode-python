# 957. Prison Cells After N Days
# https://leetcode.com/problems/prison-cells-after-n-days/

from typing import List, Dict


class Solution:
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    # we might reduce both complexity if there is loop
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        new: List[int] = [0] + cells[1:-1] + [0]
        seen: Dict[str: int] = {}
        while N:
            for i in range(1, len(cells) - 1):
                total = cells[i - 1] + cells[i + 1]
                new[i] = 0 if total == 1 else 1
            cells = new[:]
            N -= 1
            if str(cells) in seen:
                N %= seen[str(cells)] - N
            else:
                seen[str(cells)] = N
        return cells
