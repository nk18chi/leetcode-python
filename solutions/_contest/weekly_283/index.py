from typing import List, Optional, Dict, Set
from solutions._class.tree_node import TreeNode
import math


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res: List[str] = []
        for i in range(ord(s[0]), ord(s[3]) + 1):
            for j in range(int(s[1]), int(s[4]) + 1):
                cell: str = chr(i) + str(j)
                res.append(cell)
        return res

    def minimalKSum(self, nums: List[int], k: int) -> int:
        total: int = 0
        total += k * (k + 1) // 2
        nums.sort()
        index: int = 0
        _max: int = k
        while index < len(nums) and nums[index] <= _max:
            if 0 == index or nums[index - 1] < nums[index]:
                total -= nums[index]
                total += _max + 1
                _max += 1
            index += 1
        return total

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        treeDict: Dict[int, TreeNode] = {}
        childrenSet: Set[int] = set()
        for parent, child, isLeft in descriptions:
            parentNode = treeDict.setdefault(parent, TreeNode(parent))
            childNode = treeDict.setdefault(child, TreeNode(child))
            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
            childrenSet.add(child)
        root: int = (set(treeDict) - set(childrenSet)).pop()
        return treeDict[root]

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res: List[int] = []
        for n in nums:
            while True:
                x = math.gcd(res[-1] if res else 1, n)
                if x == 1:
                    break  # co-prime
                n *= res.pop() // x
            res.append(n)
        return res
