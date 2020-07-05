from typing import List, Set, Dict, Tuple


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff: int = arr[0] - arr[1]
        for i in range(2, len(arr)):
            if arr[i - 1] - arr[i] != diff:
                return False
        return True

    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        _min: int = n - min(right) if len(right) > 0 else 0
        _max: int = max(left) if len(left) > 0 else 0
        return max(_min, _max)

    def numSubmat(self, mat: List[List[int]]) -> int:
        a = mat
        n, m = len(a), len(a[0])
        f = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if a[i][j]:
                    f[i][j] = f[i][j + 1] + 1
        r = 0
        for i in range(n):
            for j in range(m):
                t = f[i][j]
                for k in range(i, n):
                    t = min(t, f[k][j])
                    if t == 0:
                        break
                    r += t
        return r
