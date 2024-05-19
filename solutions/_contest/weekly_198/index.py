from typing import List, Set, Dict, Tuple, Deque
from collections import deque, defaultdict


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res: int = numBottles
        while numBottles >= numExchange:
            res += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return res

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        childMap: Dict[int, List[int]] = {}
        for i, j in edges:
            childMap[i] = childMap.get(i, [])
            childMap[i].append(j)
            childMap[j] = childMap.get(j, [])
            childMap[j].append(i)

        res: List[int] = [0 for _ in range(n)]

        def dfs(n: int, dic: Dict[str, int], seen: Set[int]):
            seen.add(n)
            if n in childMap:
                for c in childMap[n]:
                    if c in seen:
                        continue
                    for k, v in dfs(c, {}, seen).items():
                        dic[k] = dic.get(k, 0) + v
            dic[labels[n]] = dic.get(labels[n], 0) + 1
            res[n] = dic[labels[n]]
            return dic

        dfs(0, {}, set())
        return res
