# 821. Shortest Distance to a Character - Easy
# https://leetcode.com/problems/shortest-distance-to-a-character/

from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        init = 1
        length = len(S)
        result = []
        target_count = 0
        for char in S:
            if char == C:
                init = 0
                target_count += 1
            result.append(init)
            init += 1

        count = 1
        for char in S[::-1]:
            if char == C and target_count != 0:
                init = 0
                target_count -= 1
            elif target_count == 0:
                result[length - count] = init
            else:
                if init < result[length - count]:
                    result[length - count] = init
            init += 1
            count += 1

        return result
