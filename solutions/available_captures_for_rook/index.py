# 999. Available Captures for Rook
# https://leetcode.com/problems/available-captures-for-rook/

from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        row: int = 0
        col: int = 0
        while True:
            col = 0
            while col < 8 and board[row][col] != "R":
                col += 1
            if col < 8 and board[row][col] == "R":
                break
            row += 1

        self.res: int = 0

        def helper(row: int, col: int, diff: List[int]):
            if row < 0 or row >= len(board):
                return
            if col < 0 or col >= len(board[0]):
                return
            if board[row][col] != ".":
                self.res += 1 if board[row][col].islower() else 0
                return
            helper(row + diff[0], col + diff[1], diff)

        helper(row + 1, col, [1, 0])
        helper(row, col + 1, [0, 1])
        helper(row - 1, col, [-1, 0])
        helper(row, col - 1, [0, -1])

        return self.res
