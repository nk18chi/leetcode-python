# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

from typing import List


class Solution:
    # Time complexity: O(n + e)
    # Space complexity: O(n + e)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: List[List[int]] = [[] for _ in range(numCourses)]
        indegree: List[int] = [0] * numCourses
        for _to, _from in prerequisites:
            graph[_from].append(_to)
            indegree[_to] += 1
        queue: List[int] = [i for i, x in enumerate(indegree) if x == 0]
        while queue:
            n: int = queue.pop()
            for g in graph[n]:
                indegree[g] -= 1
                if indegree[g] == 0:
                    queue.append(g)
        return sum(indegree) == 0
