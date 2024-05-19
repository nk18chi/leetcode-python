# 174. Dungeon Game
# https://leetcode.com/problems/dungeon-game/

from typing import List


class Solution:
    # Time complexity: O(mm)
    # Space complexity: O(mm)
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp: List[List[float]] = [
            [float("inf") for _ in range(len(dungeon[0]) + 1)]
            for _ in range(len(dungeon) + 1)
        ]
        dp[-1][len(dungeon[0]) - 1], dp[len(dungeon) - 1][-1] = 1, 1
        for i in range(len(dungeon) - 1, -1, -1):
            for j in range(len(dungeon[0]) - 1, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        return int(dp[0][0])
