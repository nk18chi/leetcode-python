# 884. Uncommon Words from Two Sentences
# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        list = A.split() + B.split()
        dict = {}
        for li in list:
            dict[li] = dict.get(li, 0) + 1

        res = []
        for k, v in dict.items():
            if v == 1:
                res.append(k)

        return res
