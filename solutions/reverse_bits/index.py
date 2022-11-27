# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        res: int = 0
        binary: str = bin(n)[2:]
        diff: int = 32 - len(binary)
        for i in range(32):
            if i - diff < 0:
                continue
            res += pow(2, i) * int(binary[i - diff])
        return res
