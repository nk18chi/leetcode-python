from typing import List, Optional, Set
from _class.list_node import ListNode


class Solution:
    def getSmallestString(self, s: str) -> str:
        result: str = list(s)
        for i in range(len(s) - 1):
            if int(s[i]) % 2 == int(s[i + 1]) % 2 and int(s[i]) > int(s[i + 1]):
                result[i] = s[i + 1]
                result[i + 1] = s[i]
                break
        return "".join(result)

    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        numberSet: Set[int] = set(nums)
        res: ListNode = ListNode(0)
        cur = res
        while head:
            if head.val not in numberSet:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
        return res.next

    def minimumCost(
        self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]
    ) -> int:
        horizontalCut.append(0)
        verticalCut.append(0)
        horizontalCut.sort()
        verticalCut.sort()
        sumHorizontal = sum(horizontalCut)
        sumVertical = sum(verticalCut)
        result: int = 0
        while len(horizontalCut) > 1 or len(verticalCut) > 1:
            if horizontalCut[-1] >= verticalCut[-1]:
                result += horizontalCut[-1] + sumVertical
                sumHorizontal -= horizontalCut.pop()
            else:
                result += verticalCut[-1] + sumHorizontal
                sumVertical -= verticalCut.pop()
        return result
