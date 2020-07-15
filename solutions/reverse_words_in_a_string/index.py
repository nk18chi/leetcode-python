# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

import re


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reverseWords(self, s: str) -> str:
        return "".join(re.split(r"(\s)+", s.strip())[::-1])
