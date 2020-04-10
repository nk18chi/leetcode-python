# 155. Min Stack
# https://leetcode.com/problems/min-stack/

from typing import List, Tuple, Optional


class MinStack:
    # Time complexity of each method: O(1)
    # Space complexity: O(n)
    def __init__(self):
        self.stack: List[Tuple[int, int]] = []

    def push(self, x: int) -> None:
        currentMin: Optional[int] = self.getMin()
        if currentMin is None or currentMin > x:
            currentMin = x
        self.stack.append((x, currentMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> Optional[int]:
        return self.stack[-1][0] if len(self.stack) > 0 else None

    def getMin(self) -> Optional[int]:
        return self.stack[-1][1] if len(self.stack) > 0 else None
