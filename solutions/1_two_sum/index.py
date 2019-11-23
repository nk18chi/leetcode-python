# 1. Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List


def main():
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 26))


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        for i in range(0, length):
            if target <= i:
                continue

            for j in range(i + 1, length):
                print(j)
                if target == nums[i] + nums[j]:
                    return [i, j]

        return []



if __name__ == '__main__':
    main()
