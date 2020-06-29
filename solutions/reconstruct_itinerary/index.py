# 332. Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/

from collections import defaultdict


class Solution:
    def dfs(self, airport):
        while self.adj_list[airport]:
            candidate = self.adj_list[airport].pop()
            self.dfs(candidate)
        self.route.append(airport)

    def findItinerary(self, tickets):
        self.route = []
        self.adj_list = defaultdict(list)
        for i, j in tickets:
            self.adj_list[i].append(j)
        for key in self.adj_list:
            self.adj_list[key] = sorted(self.adj_list[key], reverse=True)

        self.dfs("JFK")
        return self.route[::-1]

    # from typing import List, Dict
    # import copy

    # accepted but memories is huge
    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     destMap: Dict[str, List[str]] = defaultdict(list)
    #     for f, t in tickets:
    #         destMap[f].append(t)
    #     for arr in destMap.values():
    #         arr.sort()

    #     def dfs(start: str, destMap: Dict[str, List[str]], res: List[str]) -> List[str]:
    #         if len(res) == len(tickets) + 1:
    #             return res
    #         if start not in destMap or len(destMap[start]) == 0:
    #             return []
    #         for i in range(len(destMap[start])):
    #             newMap = copy.deepcopy(destMap)
    #             newRes = res[:]
    #             newRes.append(newMap[start].pop(i))
    #             val: List[str] = dfs(destMap[start][i], newMap, newRes)
    #             if val != []:
    #                 return val
    #         return []
    #     return dfs("JFK", destMap, ["JFK"])
