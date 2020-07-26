# 258. Add Digits
# https://leetcode.com/problems/add-digits/


class Solution:
    # Time complexity: O(?)
    # Space complexity: O(1)
    def addDigits(self, num: int) -> int:
        while num > 9:
            digitSum: int = 0
            while num:
                digitSum += num % 10
                num = num // 10
            num = digitSum
        return num
