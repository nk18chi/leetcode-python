# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

from typing import List
import copy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp: List[List[List[int]]] = [[] for _ in range(target + 1)]
        for candidate in candidates:
            for i in range(candidate, target + 1):
                if i - candidate < 0:
                    continue
                if i - candidate == 0:
                    dp[i].append([candidate])
                for sub in dp[i - candidate]:
                    p: List[int] = copy.deepcopy(sub)
                    p.append(candidate)
                    dp[i].append(p)
        return dp[target]
