# 886. Possible Bipartition
# https://leetcode.com/problems/possible-bipartition/

from typing import List, Set


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) < 3:
            return True

        while dislikes:
            left: Set[int] = set([dislikes[0][0]])
            right: Set[int] = set([dislikes[0][1]])
            nxt: List[List[int]] = []
            for i in range(len(dislikes)):
                a, b = dislikes[i]
                if a in left and b in left:
                    return False
                if a in right and b in right:
                    return False
                if a in left and b in right:
                    continue
                if b in left and a in left:
                    continue

                if a in left:
                    right.add(b)
                elif a in right:
                    left.add(b)
                elif b in left:
                    right.add(a)
                elif b in right:
                    left.add(a)
                else:
                    nxt.append([a, b])
            dislikes = nxt
        return True
