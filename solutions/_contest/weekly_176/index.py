from typing import List, Dict, Set


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"<{self.val}, {self.left}, {self.right}>"


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
        except BaseException:
            break

    return tree


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count: int = 0
        for g in grid:
            for n in g[::-1]:
                if n < 0:
                    count += 1
                else:
                    break
        return count

    # time limit exceeded
    # def maxEvents(self, events: List[List[int]]) -> int:
    #     self.max = 0

    #     def helper(self, lists: List[List[int]], checked: Set[int], count: int) -> None:
    #         if len(lists) < 1:
    #             self.max = max(self.max, count)
    #             return
    #         for li in lists:
    #             for i in range(li[0], li[1] + 1):
    #                 if i not in checked:
    #                     newList: List[List[int]] = lists[:]
    #                     newList.remove(li)
    #                     newChecked = checked.copy()
    #                     newChecked.add(i)
    #                     helper(self, newList, newChecked, count + 1)
    #                 else:
    #                     self.max = max(self.max, count)
    #                     return
    #     helper(self, events, set(), 0)
    #     return self.max

    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: (x[1], x[0]))
        used_day: Set[int] = set()
        for e in events:
            for d in range(e[0], e[1] + 1):
                if d not in used_day:
                    used_day.add(d)
                    break
        return len(used_day)

    # Input: target = [9,3,5]
    # Output: true
    # Explanation: Start with [1, 1, 1]
    # [1, 1, 1], sum = 3 choose index 1
    # [1, 3, 1], sum = 5 choose index 2
    # [1, 3, 5], sum = 9 choose index 0
    # [9, 3, 5] Done
    # def isPossible(self, target: List[int]) -> bool:
    #     target.sort()
    #     self.checked = set()
    #     self.res = False
    #     length: int = len(target)
    #     array: List[int] = [1] * length

    #     def helper(self, array: List[int], target: List[int]):
    #         if max(array) > max(target):
    #             return
    #         array.sort()
    #         if array == target:
    #             self.res = True
    #             return
    #         total: int = sum(array)
    #         if tuple(array) not in self.checked:
    #             self.checked.add(tuple(array))
    #             for i in range(length):
    #                 newArray = array[:]
    #                 newArray[i] = total
    #                 helper(self, newArray, target)
    #                 if self.res:
    #                     return
    #     helper(self, array, target)
    #     return self.res

    def isPossible(self, A):
        import bisect

        total = sum(A)
        A.sort()
        while True:
            a = A.pop()
            total -= a
            if a == 1 or total == 1:
                return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            bisect.insort(A, a)
