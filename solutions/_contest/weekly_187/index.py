from typing import List, Dict, Optional, Tuple
import heapq


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict: Dict[str, Optional[str]] = {}
        for start, dest in paths:
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

    # # TLE
    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    #     res: int = 1
    #     for i in range(len(nums)):
    #         _max = nums[i]
    #         _min = nums[i]
    #         for j in range(i + 1, len(nums)):
    #             _max = max(_max, nums[j])
    #             _min = min(_min, nums[j])
    #             if abs(_max - _min) > limit:
    #                 break
    #             else:
    #                 res = max(res, j - i + 1)
    #     return res

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq: List[Tuple[int, int]] = []
        minq: List[Tuple[int, int]] = []
        res: int = 0
        pointer: int = 0
        for i in range(len(nums)):
            heapq.heappush(maxq, (-nums[i], i))
            heapq.heappush(minq, (nums[i], i))
            while -maxq[0][0] - minq[0][0] > limit:
                pointer = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < pointer:
                    heapq.heappop(maxq)
                while minq[0][1] < pointer:
                    heapq.heappop(minq)
            res = max(res, i - pointer + 1)
        return res
