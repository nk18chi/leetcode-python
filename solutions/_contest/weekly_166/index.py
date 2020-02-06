# 733. Flood Fill - Easy
# https://leetcode.com/problems/flood-fill/

from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        sum = 0
        target = 1
        finish = False
        while (True):
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
        dict = {}
        for g in groupSizes:
            if g in dict:
                dict[g] += 1
            else:
                dict[g] = 1

        for index, value in dict.items():
            dict[index] = value / index

        list = []
        for index, value in dict.items():
            li = []
            for _ in range(int(value)):
                li = [index] * index
                list.append(li)

        for i, li in enumerate(list):
            for k, l in enumerate(li):
                id = 0
                for g in groupSizes:
                    if l == g:
                        list[i][k] = id
                        groupSizes[id] = 0
                        break
                    id += 1

        return list

    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        if len(n) < 2:
            return 0
        sum = int(n[0])
        multi = int(n[0])

        for i in n[1:]:
            sum += int(i)
            multi *= int(i)

        return multi - sum
