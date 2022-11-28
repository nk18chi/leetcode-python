# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/submissions/

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')
