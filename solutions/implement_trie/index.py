# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

from typing import Dict


class TrieNode():
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.isEnd = False


class Solution:
    # Space complexity: O(n * m), m is the length of words
    class Trie:
        def __init__(self):
            self.root = TrieNode()

        # Time complexity: O(m)
        def insert(self, word: str) -> None:
            cur = self.root
            for w in word:
                if w not in cur.children:
                    cur.children[w] = TrieNode()
                cur = cur.children[w]
            cur.isEnd = True

        # Time complexity: O(m)
        def search(self, word: str, isPrefix=False) -> bool:
            cur = self.root
            for w in word:
                if w not in cur.children:
                    return False
                cur = cur.children[w]
            return True if isPrefix else cur.isEnd

        # Time complexity: O(m)
        def startsWith(self, prefix: str) -> bool:
            return self.search(prefix, True)
