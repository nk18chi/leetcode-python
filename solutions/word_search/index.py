# 79. Word Search
# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    # Time complexity: O(?)
    # Space complexity: O(?)
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(board: List[List[str]], word: str, row: int, col: int) -> bool:
            if len(word) == 0:
                return True
            if row < 0 or row >= len(board):
                return False
            if col < 0 or col >= len(board[0]):
                return False

            if board[row][col] != word[0]:
                return False
            board[row][col] = "-"
            res: bool = helper(board, word[1:], row + 1, col) or helper(board, word[1:], row - 1,
                                                                        col) or helper(board, word[1:], row, col + 1) or helper(board, word[1:], row, col - 1)
            board[row][col] = word[0]
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if helper(board, word, i, j):
                    return True
        return False
