from typing import List, Dict, Set


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
        except BaseException:
            break

    return tree


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums: List[int] = sorted(nums)
        dict: Dict[int, int] = {sortedNums[0]: 0}
        for i in range(1, len(sortedNums)):
            if sortedNums[i - 1] < sortedNums[i]:
                dict[sortedNums[i]] = i

        res: List[int] = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] = dict[nums[i]]

        return res

    def rankTeams(self, votes: List[str]) -> str:
        count = {v: [0] * len(votes[0]) for v in votes[0]}
        for a in votes:
            for i, v in enumerate(a):
                count[v][i] -= 1
        res = ''.join(sorted(votes[0], key=lambda v: count[v] + [v]))

        # if len(votes) < 2 or len(votes[0]) < 2:
        #     return votes[0]

        # length: int = len(votes[0])
        # dict: Dict[str, int] = {}
        # for s in votes[0]:
        #     dict[s] = 0
        # for i in range(length):
        #     for vote in votes:
        #         if vote[i] in dict:
        #             dict[vote[i]] -= 1001 ** (length - i)
        res: str = "".join(k for k, v in sorted(dict.items(), key=lambda item: (item[1], item[0]), reverse=(True, False)))
        # return res
