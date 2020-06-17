# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/

from typing import List, Tuple


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(r: int, c: int, flips: List[Tuple[int, int]]):
            if r < 0 or r >= len(board):
                return False
            elif c < 0 or c >= len(board[r]):
                return False
            elif board[r][c] != "O":
                return True
            board[r][c] = "△"
            flips.append((r, c))
            return dfs(r - 1, c, flips) and dfs(r + 1, c, flips) and dfs(r, c - 1, flips) and dfs(r, c + 1, flips)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    continue
                flips: List[Tuple[int, int]] = []
                mark: str = "X" if dfs(i, j, flips) else "O"
                for r, c in flips:
                    board[r][c] = mark
