# 1137. N-th Tribonacci Number - Easy
# https://leetcode.com/problems/n-th-tribonacci-number/


class Solution:
    def tribonacci(self, n: int) -> int:
        # hashmap
        dict = {0: 0, 1: 1, 2: 1}
        for i in range(3, n + 1):
            dict[i] = dict[i - 3] + dict[i - 2] + dict[i - 1]
        return dict[n]

        # # list
        # list = [0, 1, 1]
        # for i in range(3, n + 1):
        #     list.append(list[i - 3] + list[i - 2] + list[i - 1])
        # return list[n]
