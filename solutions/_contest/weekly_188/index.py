from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res: List[str] = []
        i: int = 1
        j: int = 0
        while i <= n and j < len(target):
            res.append("Push")
            if target[j] == i:
                j += 1
            else:
                res.append("Pop")
            i += 1
        return res

    def countTriplets(self, arr: List[int]) -> int:
        res: int = 0
        i: int = 0
        while i < len(arr):
            a: int = 0
            for j in range(i, len(arr) - 1):
                a ^= arr[j]
                b: int = 0
                for k in range(j + 1, len(arr)):
                    b ^= arr[k]
                    res += 1 if a == b else 0
            i += 1
        return res
