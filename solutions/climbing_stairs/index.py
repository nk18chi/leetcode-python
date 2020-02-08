# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

from typing import List, Dict

# [1, 2]
# [1 + 1, 1 + 2, 2 + 1, 2 + 2]
# [1 + 1 + 1, 1 + 1 + 2, 1 + 2 + 1, 1 + 2 + 2, 2 + 1 + 1, 2 + 1 + 2, 2 + 2 + 1, 2 + 2 + 2]

# 1: 1
# 2: 2
# 3: 3
# 4: 5
# 5: 8


class Solution:
    # # first solution
    # def climbStairs(self, n: int) -> int:
    #     dict: Dict[int, int] = {1: 1, 2: 1}
    #     list: List[int] = [1, 2]
    #     for i in range(n - 1):
    #         cal: List[int] = []
    #         for li in list:
    #             cal.extend([li + 1, li + 2])
    #             dict[li + 1] = dict.get(li + 1, 0) + 1
    #             dict[li + 2] = dict.get(li + 2, 0) + 1
    #         list = cal

    #     return dict[n]

    # second solution
    def climbStairs(self, n: int) -> int:
        dict: Dict[int, int] = {1: 1, 2: 2}
        for i in range(3, n + 1):
            dict[i] = dict[i - 2] + dict[i - 1]
        return dict[n]
