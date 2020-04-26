from typing import List


class Solution:
    def maxScore(self, s: str) -> int:
        _max: int = 0
        for i in range(1, len(s)):
            _max = max(_max, s[:i].count("0") + s[i:].count("1"))
        return _max

    def maxScore2(self, cardPoints: List[int], k: int) -> int:
        left: List[int] = [cardPoints[0]]
        right: List[int] = [cardPoints[-1]]
        i: int = 1
        while i < k:
            left.append(left[-1] + cardPoints[i])
            right.append(right[-1] + cardPoints[-i - 1])
            i += 1
        res: int = max(left[i - 1], right[i - 1])
        i = 0
        while i < k - 1:
            res = max(res, left[i] + right[k - i - 2])
            i += 1
        return res

    # Time Limit Exceeded
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        r: int = 0
        c: int = 0
        maxRow: int = len(nums)
        reachRow: bool = False
        maxCol: int = max([len(nums[i]) for i in range(len(nums))])
        res: List[int] = []
        res.append(nums[r][c])
        while c < maxCol:
            if not reachRow and r == maxRow - 1:
                reachRow = True
            if not reachRow:
                r += 1
            else:
                c += 1
            if not reachRow:
                col: int = c
                for i in range(r, -1, -1):
                    if col < len(nums[i]):
                        res.append(nums[i][col])
                    col += 1
            else:
                row: int = r
                for i in range(c, maxCol):
                    if row < 0:
                        break
                    if i < len(nums[row]):
                        res.append(nums[row][i])
                    row -= 1
        return res
