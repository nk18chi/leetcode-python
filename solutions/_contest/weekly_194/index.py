from typing import List, Set, Dict
from collections import deque
from collections import defaultdict
import heapq


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr: List[int] = []
        for i in range(n):
            arr.append(start + i * 2)
        res: int = 0
        for a in arr:
            res ^= a
        return res

    def getFolderNames(self, names: List[str]) -> List[str]:
        setName: Dict[str, int] = defaultdict(lambda: 0)
        res: List[str] = []
        for n in names:
            if n in setName:
                i: int = setName[n]
                while True:
                    i += 1
                    name: str = n + "(" + str(i) + ")"
                    if name in setName:
                        continue
                    setName[n] = i
                    setName[name]
                    res.append(name)
                    break
            else:
                setName[n]
                res.append(n)
        return res

    def avoidFlood(self, rains: List[int]) -> List[int]:
        rainMap: Dict[int, List[int]] = defaultdict(deque)
        for i, r in enumerate(rains):
            rainMap[r].append(i)
        seen: Set[int] = set()
        res: List[int] = []
        heap: List[int] = []
        for i, r in enumerate(rains):
            if r in seen:
                return []
            if r == 0:
                if not heap:
                    res.append(1)
                    continue
                nxt = heapq.heappop(heap)
                res.append(rains[nxt])
                seen.remove(rains[nxt])
            else:
                rainMap[r].popleft()
                if rainMap[r]:
                    heapq.heappush(heap, rainMap[r][0])
                seen.add(r)
                res.append(-1)
        return res
