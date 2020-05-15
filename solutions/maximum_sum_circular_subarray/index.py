# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total: int = A[0]
        sumMax: int = A[0]
        curMax: int = A[0]
        sumMin: int = A[0]
        curMin: int = A[0]
        for i in range(1, len(A)):
            curMax = max(curMax + A[i], A[i])
            sumMax = max(sumMax, curMax)
            curMin = min(curMin + A[i], A[i])
            sumMin = min(sumMin, curMin)
            total += A[i]
        return max(sumMax, total - sumMin) if sumMax > 0 else sumMax
