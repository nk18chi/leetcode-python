# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

from typing import List


def main():
    solution = Solution()
    # print(solution.generate(0))
    # print(solution.generate(1))
    # print(solution.generate(5))
    # print(solution.generate(10))


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        initial = 1
        list = []

        if 0 == numRows:
            return list

        list.append([initial])

        for i in range(initial, numRows):
            list.append([0] * (i + 1))

            j = 0
            for li in list[i - 1]:
                list[i][j] += li
                list[i][j + 1] += li
                j += 1

        return list


if __name__ == "__main__":
    main()
