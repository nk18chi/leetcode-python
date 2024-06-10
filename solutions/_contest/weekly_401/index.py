from typing import List, Set


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        divider: int = k // (n - 1)
        mod: int = k % (n - 1)
        return mod if divider % 2 == 0 else n - 1 - mod

    def valueAfterKSeconds(self, n: int, k: int) -> int:
        arr: List[List[int]] = [[0] * n for _ in range(k + 1)]
        for i in range(n):
            for j in range(k + 1):
                if i == 0 or j == 0:
                    arr[j][i] = 1
                else:
                    arr[j][i] = arr[j - 1][i] + arr[j][i - 1]
        return arr[k][n - 1] % (10**9 + 7)

    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        pattern: Set[int] = set()
        for i in range(len(rewardValues)):
            if i > 0 and rewardValues[i] == rewardValues[i - 1]:
                continue
            for n in list(pattern):
                if n >= rewardValues[i]:
                    continue
                pattern.add(n + rewardValues[i])
            pattern.add(rewardValues[i])
        return max(pattern)
