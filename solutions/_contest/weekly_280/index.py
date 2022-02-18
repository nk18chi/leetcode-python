from typing import Dict, List, Set, Tuple


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count: int = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1
        return count

    def minimumOperations(self, nums: List[int]) -> int:
        first: Dict[int, int] = {}
        second: Dict[int, int] = {}
        for i in range(len(nums)):
            if i % 2 == 0:
                if nums[i] in first:
                    first[nums[i]] += 1
                else:
                    first[nums[i]] = 1
            else:
                if nums[i] in second:
                    second[nums[i]] += 1
                else:
                    second[nums[i]] = 1

        firstTop = sorted(first.items(), key=lambda x: x[1], reverse=True)
        firstTop.append((0, 0))
        secondTop = sorted(second.items(), key=lambda x: x[1], reverse=True)
        secondTop.append((0, 0))
        _max: int
        if (firstTop[0][0] == secondTop[0][0]):
            _max = max(firstTop[0][1] + secondTop[1][1], firstTop[1][1] + secondTop[0][1])
        else:
            _max = firstTop[0][1] + secondTop[0][1]
        return len(nums) - _max

    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        length = len(beans)
        res = beans[0] * length
        for i in range(1, len(beans)):
            if beans[i - 1] != beans[i]:
                res = max(res, beans[i] * (length - i))
        return sum(beans) - res
