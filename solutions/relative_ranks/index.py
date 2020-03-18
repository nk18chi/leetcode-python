# 506. Relative Ranks
# https://leetcode.com/problems/relative-ranks/

from typing import List, Dict


class Solution:
    # first solution
    # def findRelativeRanks(self, nums: List[int]) -> List[str]:
    #     rank: List[List[int]] = []
    #     dict: Dict[int, str] = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
    #     for i, n in enumerate(nums):
    #         rank.append([n, i])
    #     rank.sort(key=lambda x: x[0], reverse=True)
    #     for i, r in enumerate(rank):
    #         r[0] = i + 1
    #     rank.sort(key=lambda x: x[1])

    #     res: List[str] = []
    #     for r in rank:
    #         if r[0] in dict:
    #             res.append(dict[r[0]])
    #         else:
    #             res.append(str(r[0]))

    #     return res

    # second solution
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        sortedNums: List[int] = sorted(nums, reverse=True)
        rankDict: Dict[int, str] = {}
        rankNameDict: Dict[int, str] = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        for i, n in enumerate(sortedNums, 1):
            rankDict[n] = rankNameDict[i] if i in rankNameDict else str(i)

        res: List[str] = []
        for n in nums:
            res.append(rankDict[n])

        return res
