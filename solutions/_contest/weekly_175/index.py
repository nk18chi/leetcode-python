from typing import List, Dict


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
    def checkIfExist(self, arr: List[int]) -> bool:
        isZero = False
        for a in arr:
            if a == 0:
                if not isZero:
                    isZero = True
                    continue
                else:
                    return True
            if a * 2 in arr:
                return True
        return False

    def minSteps(self, s: str, t: str) -> int:
        dict: Dict[str, int] = {}
        for c1, c2 in zip(s, t):
            dict[c1] = dict.get(c1, 0) + 1
            dict[c2] = dict.get(c2, 0) - 1
        count: int = 0
        for d in dict.values():
            if d > 0:
                count += d
        return count

    class TweetCounts:
        def __init__(self):
            self.dict: Dict[str, List[int]] = {}

        def recordTweet(self, tweetName: str, time: int) -> None:
            if tweetName in self.dict:
                self.dict[tweetName].append(time)
            else:
                self.dict[tweetName] = [time]

        def getTweetCountsPerFrequency(
            self, freq: str, tweetName: str, startTime: int, endTime: int
        ) -> List[int]:
            interval: Dict[str, int] = {"minute": 60, "hour": 3600, "day": 86400}
            divide: int = interval[freq]
            self.res: List[int] = []
            tweets: List[int] = self.dict[tweetName]
            tweets.sort()

            def helper(self, tweets, start, end, divide, loopCount) -> None:
                count: List[int] = [0]
                for i in range(len(tweets)):
                    if tweets[i] < start or tweets[i] > end:
                        break
                    if tweets[i] >= divide:
                        helper(
                            self,
                            tweets[i:],
                            start,
                            end,
                            divide * loopCount,
                            loopCount + 1,
                        )
                        break
                    count[0] += 1
                self.res = count + self.res

            helper(self, tweets, startTime, endTime, divide, 2)
            return self.res
