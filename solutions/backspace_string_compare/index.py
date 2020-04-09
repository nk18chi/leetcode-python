# 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def backspaceCompare(self, S: str, T: str) -> bool:
        bs: List[int] = [0, 0]
        s: int = len(S) - 1
        t: int = len(T) - 1
        while s > -1 or t > -1:
            while s > -1 and (S[s] == "#" or bs[0]):
                bs[0] += 1 if S[s] == "#" else -1
                s -= 1
            while t > -1 and (T[t] == "#" or bs[1]):
                bs[1] += 1 if T[t] == "#" else -1
                t -= 1
            if S[s] != T[t]:
                return False
            s -= 1
            t -= 1

        return True if s == t else False

    # solution by @awice
    # # Time complexity: O(n)
    # # Space complexity: O(1)
    # import itertools
    # def backspaceCompare(self, S: str, T: str) -> bool:
    #     def F(S):
    #         skip = 0
    #         for x in reversed(S):
    #             if x == '#':
    #                 skip += 1
    #             elif skip:
    #                 skip -= 1
    #             else:
    #                 yield x

    #     return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
