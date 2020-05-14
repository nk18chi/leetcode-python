# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 0:
            return "0"
        stack: List[str] = [num[0]]
        for n in num[1:]:
            while k > 0 and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        while k > 0 and stack:
            stack.pop()
            k -= 1
        return "".join(stack).lstrip("0") or "0"
