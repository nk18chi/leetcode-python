# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

# from typing import List


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dict = {}
        for s in S:
            dict[s] = dict[s] + 1 if s in dict else 1

        total_count = 0
        for j in J:
            if j in dict:
                total_count += dict[j]

        return total_count
