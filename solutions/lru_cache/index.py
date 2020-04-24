# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

from typing import List, Dict


class Solution:
    class LRUCache:
        def __init__(self, capacity: int):
            self.cache: Dict[int, int] = {}
            self.stack: List[int] = []
            self.capacity: int = capacity

        # Time complexity: O(n)
        # Space complexity: O(n)
        def get(self, key: int) -> int:
            if key in self.cache:
                self.stack.remove(key)
                self.stack.append(key)
                return self.cache[key]
            else:
                return -1

        # Time complexity: O(n)
        # Space complexity: O(n)
        def put(self, key: int, value: int) -> None:
            if key in self.cache:
                self.stack.remove(key)
            elif len(self.cache) == self.capacity:
                del self.cache[self.stack[0]]
                self.stack.pop(0)
            self.stack.append(key)
            self.cache[key] = value
