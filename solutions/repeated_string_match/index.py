# 686. Repeated String Match
# https://leetcode.com/problems/repeated-string-match/

# from typing import List


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        # second solution
        for i in range(1, len(B) // len(A) + 3):
            if B in A * i:
                return i
        return -1

        # first solution
        # if set(A) < set(B):
        #     return - 1

        # initial = B[0]
        # dict = {initial: []}
        # for i, a in enumerate(A):
        #     if a == initial:
        #         dict[initial].append(i)

        # if len(dict[initial]) == 0:
        #     return - 1

        # for j in dict[initial]:
        #     count = 1
        #     ans = ""
        #     while (len(ans) < len(B)):
        #         ans += A[j]
        #         if j + 1 == len(A):
        #             j = 0
        #             count += 1
        #             if len(ans) == len(B) and ans == B:
        #                 return count - 1
        #         else:
        #             j += 1
        #     if ans == B:
        #         return count

        # return -1
