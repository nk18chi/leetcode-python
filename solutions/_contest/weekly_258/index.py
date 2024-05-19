from typing import List, Set, Dict, Tuple, Deque
from collections import deque, defaultdict
from _class.tree_node import TreeNode
import math


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index: int = 0
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break
        return word[: index + 1][::-1] + word[index + 1 :]

    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res: int = 0
        countMap: Dict[Tuple[int, int], int] = {}
        for rectangle in rectangles:
            gcd: int = math.gcd(rectangle[0], rectangle[1])
            key: Tuple[int, int] = (rectangle[0] // gcd, rectangle[1] // gcd)
            currentN: int = countMap.get(key, 0)
            res += currentN
            countMap[key] = currentN + 1
        return res
