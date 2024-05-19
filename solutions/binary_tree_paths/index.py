# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/

from typing import List, Optional
from _class.tree_node import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(self, node: Optional[TreeNode], cur: List[str]):
            if node is None or node.val is None:
                return
            if node.left is None and node.right is None:
                cur.append(str(node.val))
                self.res.append("->".join(cur))
                cur.pop()
                return
            cur.append(str(node.val))
            dfs(self, node.left, cur)
            dfs(self, node.right, cur)
            cur.pop()

        self.res: List[str] = []
        dfs(self, root, [])
        return self.res
