# 901. Online Stock Span
# https://leetcode.com/problems/online-stock-span/

from typing import List, Tuple


class Solution:
    # Time complexity: Amortized O(1)
    # Space complexity: O(n)
    class StockSpanner:
        def __init__(self):
            self.stack: List[Tuple[int, int]] = []

        def next(self, price: int) -> int:
            count: int = 1
            while self.stack:
                if self.stack[-1][0] > price:
                    break
                count += self.stack.pop()[1]
            self.stack.append((price, count))
            return count
