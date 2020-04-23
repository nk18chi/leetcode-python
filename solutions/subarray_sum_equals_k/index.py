# 560. Subarray Sum Equals K
# https://github.com/microsoft/vscode-python/issues/11264

from typing import List, Dict


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        res: int = 0
        total: int = 0
        countMap: Dict[int, int] = {0: 1}
        for n in nums:
            total += n
            if total - k in countMap:
                res += countMap[total - k]
            countMap[total] = countMap.get(total, 0) + 1
        return res
