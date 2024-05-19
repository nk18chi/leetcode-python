# 1221. Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced_number-strings/

# from typing import List


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # first solution
        # count = {'L': 0, 'R': 0}
        # opposite = {'L': 'R', 'R': 'L'}
        # split_count = 0
        # for c in s:
        #     count[c] += 1
        #     if count[c] == count[opposite[c]]:
        #         split_count += 1
        # return split_count

        # second solution
        split_count = balanced_number = 0
        for c in s:
            balanced_number += 1 if c == "L" else -1
            if balanced_number == 0:
                split_count += 1
        return split_count
