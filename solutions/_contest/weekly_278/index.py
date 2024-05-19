from typing import List, Set


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        sort: List[int] = sorted(nums)
        for n in sort:
            if n == original:
                original *= 2
            elif n > original:
                break
        return original

    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        res = [0]
        leftSum: int = 0
        rightSum: int = sum(1 for n in nums if n == 1)
        currentMax: int = leftSum + rightSum
        for i in range(len(nums)):
            if nums[i] == 0:
                leftSum += 1
            else:
                rightSum -= 1
            if currentMax < (leftSum + rightSum):
                res = [i + 1]
                currentMax = leftSum + rightSum
            elif currentMax == (leftSum + rightSum):
                res.append(i + 1)
        return res

    def subStrHash(
        self, s: str, power: int, modulo: int, k: int, hashValue: int
    ) -> str:
        def val(c):
            return ord(c) - ord("a") + 1

        res = n = len(s)
        pk = pow(power, k, modulo)
        cur = 0

        for i in range(n - 1, -1, -1):
            cur = (cur * power + val(s[i])) % modulo
            if i + k < n:
                cur = (cur - val(s[i + k]) * pk) % modulo
            if cur == hashValue:
                res = i
        return s[res : res + k]
