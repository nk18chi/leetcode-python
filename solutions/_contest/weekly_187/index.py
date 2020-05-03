from typing import List, Dict, Optional


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict: Dict[str, Optional[str]] = {}
        for (start, dest) in paths:
            dict[start] = dest
            if dest not in dict:
                dict[dest] = None
        for key, value in dict.items():
            if not value:
                return key
        return ""

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count: int = -1
        for n in nums:
            if count < 0 and n == 1:
                count = k
            elif n == 1:
                if count > 0:
                    return False
                count = k
            else:
                count -= 1
        return True

    # TLE
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res: int = 1
        for i in range(len(nums)):
            _max = nums[i]
            _min = nums[i]
            for j in range(i + 1, len(nums)):
                _max = max(_max, nums[j])
                _max = min(_min, nums[j])
                if abs(nums[i] - nums[j]) > limit:
                    break
                else:
                    res = max(res, j - i + 1)
        return res
