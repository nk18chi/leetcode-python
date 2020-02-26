# 547. Friend Circles
# https://leetcode.com/problems/friend-circles/

from typing import List, Set


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        self.friendRoot: List[int] = [-1] * len(M[0])
        self.checked: Set[int] = set()

        def helper(self, n: int, val: int):
            if n in self.checked:
                return
            if self.friendRoot[n] > -1:
                return

            self.friendRoot[n] = val
            self.checked.add(n)
            for i in range(len(self.friendRoot)):
                if M[n][i] == 1:
                    helper(self, i, val)

        for i in range(len(self.friendRoot)):
            helper(self, i, i)

        return len(set(self.friendRoot))
