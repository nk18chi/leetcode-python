# 941. Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/

from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        length = len(A)
        if length < 3:
            return False
        if A[0] >= A[1]:
            return False

        increase_swith = True
        for i in range(1, length - 1):
            if A[i] == A[i + 1]:
                return False
            elif A[i] > A[i + 1] and increase_swith:
                increase_swith = False
                continue
            elif A[i] <= A[i + 1] and not increase_swith:
                return False

        if increase_swith:
            return False

        return True


# class Solution:
#     def validMountainArray(self, A: List[int]) -> bool:
#         length = len(A)
#         if length < 3:
#             return False
#         if A[0] > A[1]:
#             return False

#         increase_swith = True
#         for i in range(1, length - 1):
#             if A[i] > A[i + 1] and increase_swith:
#                 increase_swith = False
#                 continue
#             elif A[i] <= A[i + 1] and not increase_swith:
#                 return False

#         if increase_swith:
#             return False

#         return True
