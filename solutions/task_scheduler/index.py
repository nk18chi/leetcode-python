# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/

from typing import List, Dict


class Solution:
    # Time complexity: O(m) m is the length of count map
    # Space complexity: O(m)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countMap: Dict[str, int] = {}
        for t in tasks:
            countMap[t] = countMap.get(t, 0) + 1
        maxNumber: int = max(countMap.values())
        maxCount: int = sum(1 for v in countMap.values() if v == maxNumber)
        return max(len(tasks), (maxNumber - 1) * (n + 1) + maxCount)
