from typing import List, Set, Dict, Tuple, Deque
from collections import deque, defaultdict
from _class.tree_node import TreeNode


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count: int = 0
        for a in arr:
            if a % 2 == 0:
                count = 0
            else:
                count += 1
                if count == 3:
                    return True
        return False
