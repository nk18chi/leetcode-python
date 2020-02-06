# 665. Non-decreasing Array
# https://leetcode.com/problems/non-decreasing-array/

from typing import List


class Solution:
    # # first solution
    # def checkPossibility(self, nums: List[int]) -> bool:
    #     decresed_count = 0
    #     last_two = [-float('inf'), nums[0]]
    #     for n in nums[1:]:
    #         if n >= last_two[1]:
    #             last_two = [last_two[1], n]
    #         else:
    #             decresed_count += 1
    #             if decresed_count > 1:
    #                 return False
    #             if last_two[0] == last_two[1]:
    #                 continue
    #             elif n < last_two[0]:
    #                 last_two = [last_two[1], last_two[1]]
    #             else:
    #                 last_two = [n, n]
    #     return True

    # second solution
    def checkPossibility(self, nums: List[int]) -> bool:
        dec_count = 0
        if len(nums) > 1 and nums[0] > nums[1]:
            dec_count += 1
            nums[0] = nums[1]

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                dec_count += 1
                if dec_count > 1:
                    return False

                if nums[i - 1] < nums[i + 1]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i + 1] = nums[i]
        return True
