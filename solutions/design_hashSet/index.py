# 705. Design HashSet
# https://leetcode.com/problems/design-hashset/


class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.set.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.set else False

    def print(self) -> None:
        return self.set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
