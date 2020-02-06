# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/


class Solution:
    # # first solution
    # def isPalindrome(self, x: int) -> bool:
    #     return str(x) == str(x)[::-1]

    # second solution(not using string)
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse, num = 0, x
        while num:
            reverse = reverse * 10 + num % 10
            num //= 10
        return x == reverse
