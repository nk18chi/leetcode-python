# 1029. Two City Scheduling
# https://leetcode.com/problems/two-city-scheduling/

from typing import List


# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda c: c[0] - c[1])
        cost_for_a = sum(cost[0] for cost in costs[: len(costs) // 2])
        cost_for_b = sum(cost[1] for cost in costs[len(costs) // 2:])
        return cost_for_a + cost_for_b

        # time exceed error
        # costs.sort(key=lambda cost: cost[0] - cost[1])
        # length = len(costs)
        # init = "0" * int(length / 2) + "1" * int(length / 2)

        # from itertools import permutations
        # patterns = set(permutations(init, len(init)))
        # print(patterns)

        # res = float('inf')
        # for pattern in patterns:
        #     sum = 0
        #     for i, p in enumerate(pattern):
        #         sum += costs[i][int(p)]
        #     res = min(res, sum)

        # return res
