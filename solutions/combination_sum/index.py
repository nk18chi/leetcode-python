# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self,
                       candidates: List[int],
                       target: int) -> List[List[int]]:
        def dfs(self, target, index, list):
            if target == 0:
                self.res.append(list)
                return
            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    break
                dfs(self, target - candidates[i], i, list + [candidates[i]])

        self.res = []
        candidates.sort()
        dfs(self, target, 0, [])
        return self.res
