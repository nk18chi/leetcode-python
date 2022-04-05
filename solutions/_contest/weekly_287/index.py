from typing import List, Dict
import math


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        count: int = 0
        currentMinutes: int = int(current[:2]) * 60 + int(current[3:])
        correctMinutes: int = int(correct[:2]) * 60 + int(correct[3:])
        diffMin: int = correctMinutes - currentMinutes
        for n in [60, 15, 5, 1]:
            count += diffMin // n
            diffMin %= n
        return count

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matchesDict: Dict[int, Dict[str, int]] = {}
        for match in matches:
            if not match[0] in matchesDict:
                matchesDict[match[0]] = {"win": 0, "lose": 0}
            if not match[1] in matchesDict:
                matchesDict[match[1]] = {"win": 0, "lose": 0}
            matchesDict[match[0]]["win"] += 1
            matchesDict[match[1]]["lose"] += 1
        res: List[List[int]] = [[], []]
        for key, value in matchesDict.items():
            if value["lose"] == 0:
                res[0].append(key)
            if value["lose"] == 1:
                res[1].append(key)
        res[0].sort()
        res[1].sort()
        return res

    def maximumCandies(self, candies: List[int], k: int) -> int:
        total: int = sum(candies)
        ans: int = 0
        left: int = 1
        right: int = total // k
        while left <= right:
            count: int = 0
            mid: int = (right + left) // 2
            for c in candies:
                count += c // mid
            if count >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
