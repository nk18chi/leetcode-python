# 687. Longest Univalue Path
# https://leetcode.com/problems/longest-univalue-path/


# def main():
#     solution = Solution()
#     object_list = [5, 4, 5, 1, 1, 5]
#     object = [TreeNode(l) for l in object_list]
#     print(object)
#     print(treenode)
#     print(solution.longestUnivaluePath(treenode))


# Definition for a binary tree node.
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.sum = 0
        self.getMaxLengthPath(root)
        return self.sum

    def getMaxLengthPath(self, node: TreeNode) -> int:
        if not node:
            return 0
        elif not node.left and not node.right:
            return 0
        else:
            l = r = 0
            if node.left:
                child = self.getMaxLengthPath(node.left)
                l = child + 1 if node.val == node.left.val else 0
            if node.right:
                child = self.getMaxLengthPath(node.right)
                r = child + 1 if node.val == node.right.val else 0

            if node.left and node.right and node.val == node.left.val == node.right.val:
                self.sum = max(self.sum, l + r)
            else:
                self.sum = max(self.sum, max(l, r))

            return max(l, r)


if __name__ == '__main__':
    main()
