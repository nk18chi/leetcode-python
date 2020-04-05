from typing import List, Dict, Set


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        res: List[int] = []
        nums.sort()
        while sum(res) <= sum(nums):
            res.append(nums.pop())
        return res

    def numSteps(self, s: str) -> int:
        step: int = 0
        n: int = int(s, 2)
        while n != 1:
            if n % 2 == 1:
                n += 1
            else:
                n = n // 2
            step += 1
        return step

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars: List[List[int]] = [[a, 0], [b, 1], [c, 2]]
        res: str = ""
        prevChar: str = ""
        count: int = 0
        while chars[0][0] + chars[1][0] + chars[2][0] > 0:
            chars.sort(key=lambda x: x[0], reverse=True)
            c: str = chr(97 + chars[0][1])
            if prevChar == c and count == 2:
                if chars[1][0] == 0:
                    break
                c = chr(97 + chars[1][1])
                chars[1][0] -= 1
            else:
                chars[0][0] -= 1
            if prevChar != c:
                count = 0
            res += c
            prevChar = c
            count += 1

        return res

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp: List[List[int]] = []
        for i, s in enumerate(stoneValue[::-1]):
            arr: List[int] = []
            a: int = s
            b: int = 0 if i - 1 < 0 else dp[i - 1][0]
            a += 0 if i - 1 < 0 else dp[i - 1][1]
            arr.append([a, b, a - b])

            if i > 0:
                a = s
                a += stoneValue[-i]
                b = 0 if i - 2 < 0 else dp[i - 2][0]
                a += 0 if i - 2 < 0 else dp[i - 2][1]
                arr.append([a, b, a - b])

            if i > 1:
                a = s
                a += stoneValue[-i]
                a += stoneValue[-i + 1]
                b = 0 if i - 3 < 0 else dp[i - 3][0]
                a += 0 if i - 3 < 0 else dp[i - 3][1]
                arr.append([a, b, a - b])
            arr.sort(key=lambda x: x[2])
            dp.append(arr[-1])
        if dp[-1][0] == dp[-1][1]:
            return "Tie"
        if dp[-1][0] > dp[-1][1]:
            return "Alice"
        else:
            return "Bob"
