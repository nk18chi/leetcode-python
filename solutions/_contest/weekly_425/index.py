from typing import List, Dict
from collections import Counter


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res: float = float("inf")
        pre: List[int] = [0]
        for n in nums:
            pre.append(pre[-1] + n)
        for i in range(l, r + 1):
            for j in range(i, len(nums) + 1):
                total: int = pre[j] - pre[j - i]
                if total > 0:
                    res = min(res, total)
        return -1 if res == float("inf") else res

    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        appear: Dict[str, int] = Counter()
        divider: int = len(s) // k
        for i in range(0, len(s), divider):
            appear[s[i : i + divider]] += 1
        for i in range(0, len(t), divider):
            appear[t[i : i + divider]] -= 1
        return all(x == 0 for x in appear.values())
