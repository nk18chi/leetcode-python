# 1035. Uncrossed Lines
# https://leetcode.com/problems/uncrossed-lines/

from typing import List


class Solution:
    # Time complexit: (mn)
    # Space complexit: (mn)
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp: List[List[int]] = [
            [0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)
        ]
        for i in range(len(A)):
            for j in range(len(B)):
                dp[i + 1][j + 1] = 1 if A[i] == B[j] else 0
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]


# func maxUncrossedLines(top []int, bottom []int) int {
# 	dp := [2][]int{}
# 	for i := range dp {
# 		dp[i] = make([]int, len(bottom)+1)
# 	}
# 	for i, n1 := range top {
# 		for j, n2 := range bottom {
# 			if n1 == n2 {
# 				dp[i&1^1][j+1] = dp[i&1][j] + 1
# 			} else {
# 				dp[i&1^1][j+1] = max(dp[i&1][j+1], dp[i&1^1][j])
# 			}
# 		}
# 	}
# 	return dp[len(top)&1][len(bottom)]
# }
