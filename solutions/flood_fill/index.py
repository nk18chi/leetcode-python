# 733. Flood Fill
# https://leetcode.com/problems/flood-fill/

from typing import List


class Solution:
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(row: int, col: int):
            if row < 0 or row >= len(image):
                return
            if col < 0 or col >= len(image[0]):
                return
            if image[row][col] != originColor:
                return
            image[row][col] = newColor
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        originColor = image[sr][sc]
        if originColor != newColor:
            dfs(sr, sc)
        return image
