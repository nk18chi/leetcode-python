# 558. Quad Tree Intersection
# https://leetcode.com/problems/quad-tree-intersection/

# from typing import List


class Node:
    def __init__(
            self,
            val,
            isLeaf,
            topLeft,
            topRight,
            bottomLeft,
            bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, qt1: 'Node', qt2: 'Node') -> 'Node':
        if not qt1 or not qt2:
            return
        if qt1.isLeaf:
            return qt1 if qt1.val else qt2
        if qt2.isLeaf:
            return qt2 if qt2.val else qt1

        qt1.topLeft = self.intersect(qt1.topLeft, qt2.topLeft)
        qt1.topRight = self.intersect(qt1.topRight, qt2.topRight)
        qt1.bottomLeft = self.intersect(qt1.bottomLeft, qt2.bottomLeft)
        qt1.bottomRight = self.intersect(qt1.bottomRight, qt2.bottomRight)

        if qt1.topLeft.isLeaf and qt1.topRight.isLeaf and qt1.bottomLeft.isLeaf and qt1.bottomRight.isLeaf and qt1.topLeft.val == qt1.topRight.val == qt1.bottomLeft.val == qt1.bottomRight.val:
            qt1.isLeaf = True
            qt1.val = qt1.topLeft.val

        return qt1

        # first solution
        # def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        #     if quadTree1.isLeaf:
        #         return quadTree1 if quadTree1.val else quadTree2
        #     elif quadTree2.isLeaf:
        #         return quadTree2 if quadTree2.val else quadTree1
        #     else:
        #         tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        #         tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
        #         bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        #         br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        #         if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
        #             node = Node(tl.val, True, None, None, None, None)
        #         else:
        #             node = Node(False, False, tl, tr, bl, br)

        #         return node
