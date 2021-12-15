from typing import List, Set, Dict
import math


class Solution:
    def countPoints(self, rings: str) -> int:
        colorDict: Dict[str, Set[str]] = {}
        for i in range(0, len(rings), 2):
            if rings[i + 1] not in colorDict:
                colorDict[rings[i + 1]] = set()
            colorDict[rings[i + 1]].add(rings[i])
        return sum(len(v) == 3 for v in colorDict.values())

    def subArrayRanges(self, nums: List[int]) -> int:
        res: int = 0
        for i in range(len(nums)):
            _min: int = nums[i]
            _max: int = nums[i]
            for j in range(i, len(nums)):
                _min = min(_min, nums[j])
                _max = max(_max, nums[j])
                res += _max - _min
        return res

    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        res: int = 0
        left: int = 0
        right: int = len(plants) - 1
        curA: int = capacityA
        curB: int = capacityB
        while left < right:
            if curA < plants[left]:
                curA = capacityA
                res += 1
            curA -= plants[left]
            if curB < plants[right]:
                curB = capacityB
                res += 1
            curB -= plants[right]
            left += 1
            right -= 1
        if left == right and plants[left] > curA and plants[left] > curB:
            res += 1
        return res
