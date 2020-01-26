from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'<{self.val}, {self.left}, {self.right}>'


def createTreeNode(list):

    from collections import deque

    data = list
    n = iter(data)
    tree = TreeNode(next(n))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            head.left = TreeNode(next(n))
            fringe.append(head.left)
            head.right = TreeNode(next(n))
            fringe.append(head.right)
        except StopIteration:
            break

    return tree


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0
        if s == s[::-1]:
            return 1

        return 2

    def filterRestaurants(self,
                          restaurants: List[List[int]],
                          veganFriendly: int,
                          maxPrice: int,
                          maxDistance: int) -> List[int]:
        res = []
        restaurants.sort(key=lambda x: (x[1], x[0]), reverse=True)
        for r in restaurants:
            if veganFriendly == 0 or r[2] == veganFriendly:
                if r[3] <= maxPrice:
                    if r[4] <= maxDistance:
                        res.append(r[0])
        return res

    # def findTheCity(self,
    #                 n: int,
    #                 edges: List[List[int]],
    #                 distanceThreshold: int) -> int:
    #     dict = {}
    #     for i in range(n):
    #         dict[i] = [i]

    #     def helper(self, distance, num, index):
    #         if distance <= 0:
    #             return
    #         for e in edges:
    #             if e[0] == num and e[2] <= distance:
    #                 if not e[1] in dict[index]:
    #                     dict[index].append(e[1])
    #                 helper(self, distance - e[2], e[1], index)
    #             elif e[1] == num and e[2] <= distance:
    #                 if not e[0] in dict[index]:
    #                     dict[index].append(e[0])
    #                 helper(self, distance - e[2], e[0], index)

    #     for i in range(n):
    #         helper(self, distanceThreshold, i, i)

    #     index = 0
    #     _min = float('inf')
    #     for k, v in dict.items():
    #         if _min >= len(v):
    #             _min = len(v)
    #             index = k

    #     return index
