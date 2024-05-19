# 733. Flood Fill - Easy
# https://leetcode.com/problems/flood-fill/

from typing import List, Dict


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        sum: int = 0
        target: int = 1
        finish: bool = False
        while True:
            for n in nums:
                import math

                sum += math.ceil(n / target)
                if sum > threshold:
                    target += 1
                    sum = 0
                    finish = False
                    break
                else:
                    finish = True
            if finish:
                return target

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict: Dict[int, int] = {}
        for g in groupSizes:
            if g in dict:
                dict[g] += 1
            else:
                dict[g] = 1

        for index, value in dict.items():
            dict[index] = value // index

        list: List[List[int]] = []
        for index, value in dict.items():
            li = []
            for _ in range(int(value)):
                li = [index] * index
                list.append(li)

        for i, li in enumerate(list):
            for k, _l in enumerate(li):
                id = 0
                for g in groupSizes:
                    if _l == g:
                        list[i][k] = id
                        groupSizes[id] = 0
                        break
                    id += 1

        return list

    def subtractProductAndSum(self, n: int) -> int:
        str_n: str = str(n)
        if len(str_n) < 2:
            return 0
        sum = int(str_n[0])
        multi = int(str_n[0])

        for i in str_n[1:]:
            sum += int(i)
            multi *= int(i)

        return multi - sum
