from typing import List


class BinaryMatrix(object):
    def __init__(self, arr: List[int]):
        self.matrix = arr

    def get(self, x: int, y: int) -> int:
        return self.matrix[x][y]

    def dimensions(self) -> List[int]:
        return [len(self.matrix), len(self.matrix[0])]
