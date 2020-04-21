# Leftmost Column with at Least a One
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/


from solutions._class.binary_matrix import BinaryMatrix


class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(1)
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row: int
        col: int
        row, col = binaryMatrix.dimensions()
        n: int = 0
        m: int = col - 1
        while n < row and m >= 0:
            if binaryMatrix.get(n, m) == 1:
                m -= 1
            else:
                n += 1
        return -1 if m == col - 1 else 0 if m < 0 else m + 1

    # # Time complexity: O(n * logm)
    # # Space complexity: O(n)
    # def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    #     r, c = binaryMatrix.dimensions()
    #     rows: Set[int] = {i for i in range(r)}

    #     left, right = 0, c - 1
    #     while left <= right:
    #         mid: int = (left + right) // 2
    #         isContinue: bool = False
    #         newRows: Set[int] = rows.copy()
    #         for r in rows:
    #             if binaryMatrix.get(r, mid) == 0:
    #                 newRows.remove(r)
    #             elif mid > 0 and binaryMatrix.get(r, mid - 1) == 1:
    #                 isContinue = True
    #                 break
    #         if len(newRows) < 1:
    #             left = mid + 1
    #         elif not isContinue:
    #             return mid
    #         else:
    #             rows = newRows
    #             right = mid - 1
    #     return 0 if right < 0 else -1
