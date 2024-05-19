# 1044. Longest Duplicate Substring
# https://leetcode.com/problems/longest-duplicate-substring/

# from typing import List
from functools import reduce


class Solution:
    # answer by @lee215
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def longestDupSubstring(self, S):
        A = [ord(c) - ord("a") for c in S]
        mod = 2**63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen:
                    return i - L + 1
                seen.add(cur)

        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res : res + lo]
