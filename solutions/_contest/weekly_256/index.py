from typing import List, Dict


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sortedNums: List[int] = sorted(nums)
        res: float = float('inf')
        for i in range(len(sortedNums) - k + 1):
            diff = sortedNums[i + k - 1] - sortedNums[i]
            res = min(diff, res)
        return int(res)

    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return sorted(nums, key=int)[-k]

    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        self.ans: int = len(tasks)
        self.sessions: List[int] = []

        def dfs(index: int):
            if len(self.sessions) >= self.ans:
                return
            if index >= len(tasks):
                self.ans = min(self.ans, len(self.sessions))
                return

            for i in range(len(self.sessions)):
                if self.sessions[i] + tasks[index] <= sessionTime:
                    self.sessions[i] += tasks[index]
                    dfs(index + 1)
                    self.sessions[i] -= tasks[index]

            self.sessions.append(tasks[index])
            dfs(index + 1)
            self.sessions.pop()
        dfs(0)
        return self.ans
