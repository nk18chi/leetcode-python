# Counting Elements
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/

from typing import List, Set


class Solution:
    def countElements(self, arr: List[int]) -> int:
        setArr: Set = set(arr)
        res: int = 0
        for a in arr:
            if a + 1 in setArr:
                res += 1
        return res
