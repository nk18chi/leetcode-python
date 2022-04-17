from typing import List, Dict


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            text: str = ""
            n: int = 0
            for i in range(len(s)):
                if i > 0 and i % k == 0:
                    text += str(n)
                    n = 0
                n += int(s[i])
            text += str(n)
            s = text
        return s

    def minimumRounds(self, tasks: List[int]) -> int:
        countDict: Dict[int, int] = {}
        for t in tasks:
            if t not in countDict:
                countDict[t] = 0
            countDict[t] += 1
        count: int = 0
        dpDict: Dict[int, int] = {2: 1, 3: 1, 4: 2}
        maxDp: int = 4
        for value in countDict.values():
            if value == 1:
                return -1
            while maxDp < value:
                maxDp += 1
                dpDict[maxDp] = min(dpDict[maxDp - 2] + 1, dpDict[maxDp - 3] + 1)
            count += dpDict[value]
        return count

    # def maxTrailingZeros(self, grid: List[List[int]]) -> int:
    #     def trailing(n):
    #         res: int = 0
    #         while n % 10 == 0:
    #             n /= 10
    #             res += 1
    #         return res

    #     vDp: List[int] = []
    #     hDp: List[int] = []
    #     for i in range(len(grid)):
    #         vProduct: int = 1
    #         hProduct: int = 1
    #         for j in range(len(grid[i])):
    #             vProduct *= grid[i][j]
    #             hProduct *= grid[j][i]
    #         vDp.append(vProduct)
    #         hDp.append(hProduct)
    #     count: int = 0
    #     vCur: int = 1
    #     for i in range(len(grid)):
    #         hCur: int = 1
    #         for j in range(len(grid[i])):
    #             hCur *= grid[i][j]
    #             print(vDp[j], hDp[i], hCur)
    #             print(vDp[j], hCur, grid[i][j])
    #             res1 = trailing((vDp[j] / vCur) * (hDp[i] / hCur))
    #             res2 = trailing(vDp[j] * hCur / grid[i][j] / vCur)
    #             count = max(count, res1)
    #             count = max(count, res2)
    #         vCur *= grid[i][0]
    #     for i in range(len(grid) - 1, -1, -1):
    #         hCur = 1
    #         for j in range(len(grid[i]) - 1, -1, -1):
    #             hCur *= grid[i][j]
    #             res1 = trailing(vDp[j] * hDp[i] / hCur)
    #             res2 = trailing(vDp[j] * hCur / grid[i][j])
    #             count = max(count, res1)
    #             count = max(count, res2)

    #     return count
