# 1005. Maximize Sum Of Array After K Negations
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for i in range(K):
            if A[i] < 0:
                A[i] *= -1
            elif A[i] == 0:
                break
            else:
                if (K - i + 1) % 2 == 0:
                    if A[i - 1] < A[i]:
                        A[i - 1] *= -1
                    else:
                        A[i] *= -1
                break
        return sum(A)
