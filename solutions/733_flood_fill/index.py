# 733. Flood Fill
# # https://leetcode.com/problems/flood-fill/

from typing import List


class Solution:
    def floodFill(self,
                  image: List[List[int]],
                  sr: int,
                  sc: int,
                  newColor: int) -> List[List[int]]:

        self.max_heigh = len(image)
        self.max_width = len(image[0])
        self.image = image
        self.newColor = newColor
        self.prevColor = self.image[sr][sc]
        self.fillSquare(sr, sc)

        return self.image

    def fillSquare(self, r, c):
        if r < 0 or r >= self.max_heigh:
            return
        elif c < 0 or c >= self.max_width:
            return
        elif self.image[r][c] != self.prevColor:
            return
        else:
            self.image[r][c] = -1
            self.fillSquare(r + 1, c)
            self.fillSquare(r - 1, c)
            self.fillSquare(r, c + 1)
            self.fillSquare(r, c - 1)
            self.image[r][c] = self.newColor
