# 1344. Angle Between Hands of a Clock
# https://leetcode.com/problems/angle-between-hands-of-a-clock/


class Solution:
    # Time complexity: O(1)
    # Space complexity: O(1)
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        short: float = hour * 30 + minutes * 0.5
        long: int = minutes * 6
        ans: float = abs(long - short)
        return min(ans, 360 - ans)
