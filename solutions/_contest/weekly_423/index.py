from typing import List, Dict
from collections import Counter


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        result: int = 1
        count: int = [1, 1]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                count[1] += 1
            else:
                count[0], count[1] = count[1], 1
            result = max(result, min(count[0], count[1]), count[1] // 2)
        return result >= k

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        result: int = 1
        count: int = [1, 1]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                count[1] += 1
            else:
                count[0], count[1] = count[1], 1
            result = max(result, min(count[0], count[1]), count[1] // 2)
        return result

    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        counter: Dict[int, int] = Counter()
        dp: Dict[int, int] = Counter()
        for n in nums:
            x: int = counter[n - 1] + counter[n + 1] + 1
            counter[n] += x
            dp[n] += x * n + dp[n - 1] + dp[n + 1]
        return sum(dp.values()) % (10**9 + 7)
