# 60. Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/

from typing import List


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def getPermutation(self, n: int, k: int) -> str:
        arr: List[int] = [x for x in range(1, n + 1)]
        res: str = ""
        factorial: List[int] = [1]
        for i in range(1, n):
            factorial.append(factorial[i - 1] * i)
        k -= 1
        for i in range(n, 0, -1):
            id = k // factorial[i - 1]
            k %= factorial[i - 1]
            res += str(arr[id])
            arr.pop(id)
        return res
