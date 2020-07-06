# 66. Plus One
# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        isAdd: bool = True
        for i in range(len(digits) - 1, -1, -1):
            if isAdd is False:
                break
            if digits[i] == 9:
                digits[i] = 0
                continue
            digits[i] += 1
            isAdd = False
        if isAdd:
            digits.insert(0, 1)
        return digits
