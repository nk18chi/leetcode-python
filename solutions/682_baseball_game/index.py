# 682. Baseball Game
# https://leetcode.com/problems/baseball-game/

from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # first solution
        # valid_list = []
        # score = 0
        # for o in ops:
        #     if o == "D":
        #         sum = valid_list[-1] * 2
        #         score += sum
        #         valid_list.append(sum)
        #     elif o == "C":
        #         score -= valid_list[-1]
        #         valid_list = valid_list[:-1]
        #     elif o == "+":
        #         sum = 0
        #         for e in valid_list[-2:]:
        #             sum += e
        #         score += sum
        #         valid_list.append(sum)
        #     else:
        #         integer = int(o)
        #         score += integer
        #         valid_list.append(integer)
        # return score

        # second solution
        history = []
        for o in ops:
            if o == "D":
                history.append(history[-1] * 2)
            elif o == "C":
                history.pop()
            elif o == "+":
                history.append(history[-1] + history[-2])
            else:
                history.append(int(o))

        return sum(history)
