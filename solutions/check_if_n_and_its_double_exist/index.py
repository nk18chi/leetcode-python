# 1346. Check If N and Its Double Exist
# https://leetcode.com/problems/check-if-n-and-its-double-exist/

from typing import List, Set


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(2n) -> O(n)
    def checkIfExist(self, arr: List[int]) -> bool:
        seen: Set[int] = set()
        for a in arr:
            if a in seen:
                return True
            seen.add(a * 2)
            if a % 2 == 0:
                seen.add(a // 2)
        return False
