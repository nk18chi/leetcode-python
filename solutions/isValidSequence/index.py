# Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/

from typing import List
from solutions._class.tree_node import TreeNode


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(root: TreeNode, index: int) -> bool:
            if not root or len(arr) <= index or root.val != arr[index]:
                return False
            elif len(arr) == index + 1 and not root.left and not root.right:
                return True
            return dfs(root.left, index + 1) or dfs(root.right, index + 1)
        return dfs(root, 0)
