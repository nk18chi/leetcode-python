from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def maxSubarrayLength(self, badges):
        count: int = 0
        pos: List[int] = [len(badges) - 1, 0]
        for i in range(len(badges)):
            if badges[i] == -1:
                pos[0] = min(pos[0], i)
                pos[1] = max(pos[1], i)
                count += 1
        if count % 2 == 0:
            return len(badges)
        return max(len(badges[pos[0] + 1 :]), len(badges[: pos[1]]))

    def getImbalanceRank(self, ranks):
        count: int = 0
        for i in range(len(ranks)):
            target: int = ranks[i]
            leftLen: int = 0
            leftLow: int = 0
            l: int = i - 1
            while 0 <= l and ranks[l] != target + 1:
                if ranks[l] < target and leftLen == leftLow:
                    leftLow += 1
                leftLen += 1
                l -= 1

            rightLen: int = 0
            rightLow: int = 0
            r: int = i + 1
            while r < len(ranks) and ranks[r] != target + 1:
                if ranks[r] < target and rightLen == rightLow:
                    rightLow += 1
                rightLen += 1
                r += 1

            count += (
                (leftLen - leftLow) * (rightLen - rightLow)
                + (leftLen - leftLow) * (rightLow + 1)
                + (rightLen - rightLow) * (leftLow + 1)
            )

        return count
