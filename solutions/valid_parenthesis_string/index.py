# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def checkValidString(self, s):
        _min: int = 0
        _max: int = 0
        for c in s:
            if c == "(":
                _min += 1
                _max += 1
            elif c == ")":
                _min -= 1
                _max -= 1
            else:
                _min -= 1
                _max += 1
            if _max < 0:
                return False
            _min = max(_min, 0)
        return _min == 0
