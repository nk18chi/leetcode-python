from typing import List, Set, Dict, Tuple, Deque
from collections import deque, defaultdict
from _class.tree_node import TreeNode


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res: int = 0
        for one in range(len(nums)):
            for two in range(one + 1, len(nums)):
                for three in range(two + 1, len(nums)):
                    for four in range(three + 1, len(nums)):
                        if nums[one] + nums[two] + nums[three] == nums[four]:
                            res += 1
        return res

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        curr_max = 0
        for _, d in properties:
            if d < curr_max:
                ans += 1
            else:
                curr_max = d
        return ans
