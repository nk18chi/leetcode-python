from typing import List, Set, Dict, Tuple, Deque
from collections import deque


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        res: List[float] = [0 for _ in range(n)]
        graph: Dict[int, List[Tuple[int, float]]] = {}
        for i in range(len(edges)):
            if edges[i][0] in graph:
                graph[edges[i][0]].append((edges[i][1], succProb[i]))
            else:
                graph[edges[i][0]] = [(edges[i][1], succProb[i])]
            if edges[i][1] in graph:
                graph[edges[i][1]].append((edges[i][0], succProb[i]))
            else:
                graph[edges[i][1]] = [(edges[i][0], succProb[i])]
        queue: Deque[Tuple[int, float]] = deque([(start, 1)])
        res[start] = 1
        while queue:
            cur, pos = queue.popleft()
            if cur == end:
                continue
            if cur not in graph:
                continue
            for n, pro in graph[cur]:
                if res[n] < pos * pro:
                    res[n] = pos * pro
                    queue.append((n, res[n]))
        return res[end]
