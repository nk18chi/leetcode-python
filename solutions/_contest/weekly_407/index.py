from typing import List


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        x: str = bin(n)[2:]
        y: str = bin(k)[2:]
        x = x.zfill(len(y))
        y = y.zfill(len(x))
        result: int = 0
        for i in range(len(x)):
            if x[i] == "0" and y[i] == "1":
                return -1
            if x[i] == "1" and y[i] == "0":
                result += 1
        return result

    def doesAliceWin(self, s: str) -> bool:
        for c in s:
            if c in ["a", "e", "i", "o", "u"]:
                return True
        return False

    def maxOperations(self, s: str) -> int:
        count: int = 0
        n: int = 0
        for i in range(len(s)):
            if s[i] == "1":
                n += 1
            elif i == len(s) - 1 or s[i + 1] != "0":
                count += n
        return count

    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        diff: List[int] = []
        for i in range(len(nums)):
            diff.append(nums[i] - target[i])
        count: int = abs(diff[0])
        for i in range(1, len(diff)):
            if diff[i] >= 0 and diff[i - 1] >= 0:
                if diff[i - 1] <= diff[i]:
                    count += diff[i] - diff[i - 1]
            elif diff[i] <= 0 and diff[i - 1] <= 0:
                if diff[i - 1] >= diff[i]:
                    count += abs(diff[i] - diff[i - 1])
            else:
                count += abs(diff[i])
        return count
