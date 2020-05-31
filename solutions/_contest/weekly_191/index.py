from typing import List, Set, Dict


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2] - 1) * (nums[-1] - 1)

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.sort()
        verticalCuts.append(w)
        hMax: int = horizontalCuts[0]
        vMax: int = verticalCuts[0]
        for i in range(1, len(horizontalCuts)):
            hMax = max(hMax, horizontalCuts[i] - horizontalCuts[i - 1])
        for i in range(1, len(verticalCuts)):
            vMax = max(vMax, verticalCuts[i] - verticalCuts[i - 1])
        return hMax * vMax % (10**9 + 7)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        pathMap: Dict[int, List[List[int]]] = {}
        for i in range(n):
            pathMap[i] = [[], []]
        for _from, _to in connections:
            pathMap[_from][1].append(_to)
            pathMap[_to][0].append(_from)
        queue: List[int] = [0]
        seen: Set[int] = set()
        count: int = 0
        while len(queue) > 0:
            nxt: List[int] = []
            while len(queue) > 0:
                val: int = queue.pop()
                if val in seen:
                    continue
                seen.add(val)
                tmp = [x for x in pathMap[val][1] if x not in seen]
                count += len(tmp)
                nxt.extend(tmp)
                nxt.extend(pathMap[val][0])
            queue = nxt
        return count
