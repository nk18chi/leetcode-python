# 231. Power of Two - Easy
# https://leetcode.com/problems/power-of-two/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # first solution
        if n == 0:
            return False
        str = format(n, 'b')
        for s in str[1:]:
            if int(s) == 1:
                return False

        return True

        # # second solution
        # if n == 0:
        #     return False
        # if n == 1:
        #     return True
        # i = int(format(n, 'b')[1:])
        # if i == 0:
        #     return True
        # return False
