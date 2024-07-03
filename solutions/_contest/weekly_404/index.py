from typing import List


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def check(balls: List[int]) -> int:
            row: int = 1
            while True:
                index: int = (row + 1) % 2
                balls[index] -= row
                if balls[index] < 0:
                    row -= 1
                    break
                row += 1
            return row

        return max(check([red, blue]), check([blue, red]))

    def maximumLength(self, nums: List[int]) -> int:
        odd: int = 0
        even: int = 0
        mix: int = 0
        mix_prev: int = nums[0] % 2 + 1
        for n in nums:
            if n % 2 == 0:
                even += 1
            else:
                odd += 1
            if n % 2 != mix_prev:
                mix += 1
                mix_prev = n % 2
        return max(odd, even, mix)

    def maximumLength2(self, nums: List[int], k: int) -> int:
        dp: List[int] = [[0] * k for _ in range(k)]
        result: int = 0

        for num in nums:
            remainder = num % k
            for j in range(k):
                dp[remainder][j] = max(dp[remainder][j], dp[j][remainder] + 1)
                result = max(result, dp[remainder][j])
        return result
