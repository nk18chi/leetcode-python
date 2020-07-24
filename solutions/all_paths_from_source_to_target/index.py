# 797. All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import List


class Solution:
    # Time complexity: O(2^N)
    # Space complexity: O(2^N)
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res: List[List[int]] = []
        dest: int = len(graph) - 1

        def dfs(cur: int, path: List[int]):
            if cur == dest:
                res.append(path[:])
                return
            for i in graph[cur]:
                dfs(i, path + [i])
        dfs(0, [0])
        return res
