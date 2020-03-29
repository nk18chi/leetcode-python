# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses

from typing import List


class Solution:
    # # first solution(dp)
    # def generateParenthesis(self, n: int) -> List[str]:
    #     dp: List[List[str]] = [[] for _ in range(n + 1)]
    #     dp[0].append('')
    #     for i in range(1, n + 1):
    #         for j in range(i):
    #             for p1 in dp[i - j - 1]:
    #                 for p2 in dp[j]:
    #                     dp[i] += ["(" + p2 + ")" + p1]
    #     return dp[n]

    # second solution(dfs)
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(lft: int, rgt: int, s: str):
            if lft == 0 and rgt == 0:
                res.append(s)
            if lft > 0:
                dfs(lft - 1, rgt, s + "(")
            if rgt > 0 and lft < rgt:
                dfs(lft, rgt - 1, s + ")")

        res: List[str] = []
        left: int = n
        right: int = n
        dfs(left, right, "")
        return res
