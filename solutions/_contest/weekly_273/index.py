from typing import List


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return num % 10 != 0

    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res: List[int] = []
        for i in range(len(s)):
            count: int = 0
            pos: List[int] = [startPos[0], startPos[1]]
            for j in range(len(s[i:])):
                if s[i:][j] == "R":
                    pos[1] += 1
                elif s[i:][j] == "L":
                    pos[1] -= 1
                elif s[i:][j] == "D":
                    pos[0] += 1
                elif s[i:][j] == "U":
                    pos[0] -= 1

                if pos[0] < 0 or n <= pos[0]:
                    break
                elif pos[1] < 0 or n <= pos[1]:
                    break
                else:
                    count += 1
            res.append(count)
        return res
