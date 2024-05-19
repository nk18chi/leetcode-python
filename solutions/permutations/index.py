# 46. Permutations
# https://leetcode.com/problems/permutations/

from typing import List

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i:] + nums[:i])
        length = len(nums)
        index = length - 1
        while index > 1:
            res = []
            for a in ans:
                fix = a[: length - index]
                list = a[length - index :]
                for i in range(1, len(list)):
                    res.append(fix + list[i:] + list[:i])
            ans.extend(res)
            index -= 1

        return ans
