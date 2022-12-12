# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/

from solutions._class.node import Node


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(N)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        res = Node(node.val)
        history = {}
        history[node.val] = res
        stack = [node]
        while len(stack) > 0:
            cur = stack.pop()
            for n in cur.neighbors:
                if n.val not in history:
                    stack.append(n)
                    history[n.val] = Node(n.val)
                history[cur.val].neighbors.append(history[n.val])
        return res
