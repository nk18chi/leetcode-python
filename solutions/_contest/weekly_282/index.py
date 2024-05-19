from typing import Dict, List, Set, Tuple
import math


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count: int = 0
        length: int = len(pref)
        for word in words:
            if word[:length] == pref:
                count += 1
        return count

    def minSteps(self, s: str, t: str) -> int:
        charMap: Dict[str, int] = {}
        for i in range(len(s)):
            if s[i] not in charMap:
                charMap[s[i]] = 0
            charMap[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in charMap:
                charMap[t[i]] = 0
            charMap[t[i]] -= 1
        count: int = 0
        for value in charMap.values():
            count += abs(value)
        return count

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        r = min(time) * totalTrips
        ans = float("inf")
        while l <= r:
            mid = l + (r - l) // 2
            cur = 0
            for t in time:
                cur += mid // t
            if cur < totalTrips:
                l = mid + 1
            else:
                ans = min(mid, ans)
                r = mid - 1
        return ans

    def minimumFinishTime(
        self, tires: List[List[int]], changeTime: int, numLaps: int
    ) -> int:
        minimum = []
        total = [0] * len(tires)
        while True:
            for t in range(len(tires)):
                total[t] += tires[t][0]
                tires[t][0] *= tires[t][1]
            minimum.append(min(total))
            if minimum[-1] > changeTime + minimum[0]:
                break

        dp = [float("inf")] * numLaps
        for l in range(numLaps):
            for pre in range(len(minimum)):
                if l - pre - 1 < 0:
                    dp[l] = min(dp[l], minimum[pre])
                    break
                dp[l] = min(dp[l], minimum[pre] + dp[l - pre - 1] + changeTime)
        return dp[-1]
