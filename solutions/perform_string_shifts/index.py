# Perform String Shifts - 30-Day LeetCoding Challenge Day 14
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

from typing import List


class Solution:
    # Time complexity: O(n * m)
    # Space complexity: O(m)
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for arr in shift:
            s = (
                s[arr[1] :] + s[: arr[1]]
                if arr[0] == 0
                else s[-arr[1] :] + s[: -arr[1]]
            )
        return s
