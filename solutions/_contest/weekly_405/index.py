from typing import List


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k = k % len(s)
        return s[k:] + s[:k]

    def validStrings(self, n: int) -> List[str]:
        result: List[int] = ["0", "1"]
        count: int = 1
        while n > count:
            newResult: List[int] = []
            for s in result:
                if s[-1] == "0":
                    newResult.append(s + "1")
                else:
                    newResult.append(s + "0")
                    newResult.append(s + "1")
            result = newResult
            count += 1
        return result

    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        result: int = 0
        dp = [[[0, 0] for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]
        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                dp[i][j][0] = dp[i - 1][j][0] + dp[i][j - 1][0] - dp[i - 1][j - 1][0]
                dp[i][j][1] = dp[i - 1][j][1] + dp[i][j - 1][1] - dp[i - 1][j - 1][1]
                if grid[i - 1][j - 1] == "X":
                    dp[i][j][0] += 1
                elif grid[i - 1][j - 1] == "Y":
                    dp[i][j][1] += 1
                if dp[i][j][0] > 0 and dp[i][j][0] == dp[i][j][1]:
                    result += 1
        return result
