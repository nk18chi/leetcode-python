# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

from typing import List, Set


class Solution:
    # Time complexity: O(N^2)
    # Space complexity: O(N^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: List[Set[str]] = [set() for _ in range(len(board))]
        columns: List[Set[str]] = [set() for _ in range(len(board))]
        squares: List[Set[str]] = [set() for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows[row]:
                    return False
                if board[row][col] in columns[col]:
                    return False
                if board[row][col] in squares[(row // 3) * 3 + (col // 3)]:
                    return False
                rows[row].add(board[row][col])
                columns[col].add(board[row][col])
                squares[(row // 3) * 3 + (col // 3)].add(board[row][col])
        return True
