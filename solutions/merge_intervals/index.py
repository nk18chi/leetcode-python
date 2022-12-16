# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

from typing import List


class Solution:
    # Time complexity: O(Nlog(N))
    # Space complexity: O(N)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res: List[List[int]] = [intervals[0]]
        for i in range(len(intervals)):
            last: List[int] = res.pop()
            if last[0] <= intervals[i][0] and last[1] >= intervals[i][0]:
                res.append([last[0], max(last[1], intervals[i][1])])
            else:
                res.append(last)
                res.append(intervals[i])
        return res
