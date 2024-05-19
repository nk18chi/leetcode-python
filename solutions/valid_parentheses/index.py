# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        dict = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in dict.values():
                stack.append(c)
            elif c in dict.keys():
                if not stack or dict[c] != stack.pop():
                    return False
            else:
                return False

        return len(stack) == 0
