# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/

from typing import List, Dict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        import collections
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(nei, target) for nei in graph[source])

        res = []
        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                res = [u, v]
            graph[u].add(v)
            graph[v].add(u)
        return res
