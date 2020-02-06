# 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def bs(self, start, end):
            if start > end:
                return 0

            length = end + start + 1
            mid = length // 2
            if letters[mid - 1] <= target and target < letters[mid]:
                return mid
            if target >= letters[mid]:
                return bs(self, mid + 1, end)
            else:
                return bs(self, start, mid - 1)

        i = bs(self, 0, len(letters) - 1)
        return letters[i]
