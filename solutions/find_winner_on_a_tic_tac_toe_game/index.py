# 1275. Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

from typing import List
import copy


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        pattern_a = [
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]]
        ]

        pattern_b = copy.deepcopy(pattern_a)

        for i, m in enumerate(moves, 1):
            if i % 2 == 1:
                for a in pattern_a:
                    if m in a:
                        a.remove(m)
                        if len(a) == 0:
                            return "A"
            else:
                for b in pattern_b:
                    if m in b:
                        b.remove(m)
                        if len(b) == 0:
                            return "B"
        if i < 9:
            return "Pending"
        return "Draw"
