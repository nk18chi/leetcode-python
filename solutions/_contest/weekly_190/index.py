from typing import List, Set, Dict
from solutions._class.tree_node import TreeNode


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr: List[str] = sentence.split(" ")
        for i, a in enumerate(arr):
            if a[:len(searchWord)] == searchWord:
                return i + 1
        return -1

    def maxVowels(self, s: str, k: int) -> int:
        char: Set[str] = set(["a", "e", "u", "i", "o"])
        res: int = 0
        for c in s[:k]:
            if c in char:
                res += 1
        _max: int = res
        for i in range(k, len(s)):
            if s[i] in char:
                res += 1
            if s[i - k] in char:
                res -= 1
            _max = max(_max, res)
        return res

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.res: int = 0

        def dfs(root: TreeNode, dict: Dict[str, int]):
            if root is None:
                return
            dict[root.val] = dict.get(root.val, 0) + 1
            left: TreeNode = dfs(root.left, dict)
            right: TreeNode = dfs(root.right, dict)
            if left is None and right is None:
                check(dict)
            dict[root.val] -= 1
            return 0

        def check(d: Dict[str, int]):
            isOdd: int = 0
            for val in d.values():
                if val % 2 == 1:
                    isOdd += 1
                    if isOdd > 1:
                        break
            if isOdd < 2:
                self.res += 1
        dfs(root, {})
        return self.res

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp: List[List[int]] = [[-1001 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i + 1][j + 1] = nums1[i] * nums2[j]
                dp[i + 1][j + 1] += dp[i][j] if dp[i][j] > 0 else 0
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]
