# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

from typing import List


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(1)
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res: List[List[int]] = []
        start: int = newInterval[0]
        end: int = newInterval[1]
        i = 0
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                i -= 1
                break
            else:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
        res.append([start, end])
        res += intervals[i + 1 :]
        return res
