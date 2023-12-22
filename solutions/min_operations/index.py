# 2870. Minimum Number of Operations to Make Array Empty
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/

from typing import List, Dict


class Solution:
    # Time complexity: O()
    # Space complexity: O()
    def minOperations(self, nums: List[int]) -> int:
        counterDict: Dict[int, int] = {}
        for num in nums:
            counterDict[num] = counterDict.get(num, 0) + 1
        count: int = 0
        dp: List[int] = [0, -1, 1, 1, 2]
        for value in counterDict.values():
            while len(dp) <= value:
                dp.append(min(dp[-2], dp[-3]) + 1)
            if dp[value] == -1:
                count = -1
                break
            count += dp[value]
        return count
