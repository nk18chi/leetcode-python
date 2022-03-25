from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count: int = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i - 1]
            elif nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                count += 1
            elif nums[i - 1] > nums[i] and nums[i] < nums[i + 1]:
                count += 1
        return count

    def countCollisions(self, directions: str) -> int:
        d: List[str] = list(directions)
        count: int = 0
        beforeCount: int = 0
        for i in range(1, len(d)):
            if d[i - 1] == "R" and d[i] == "L":
                count += 2 + beforeCount
                d[i] = "S"
            elif d[i - 1] == "S" and d[i] == "L":
                count += 1
                d[i] = "S"
            elif d[i - 1] == "R" and d[i] == "S":
                count += 1 + beforeCount
            elif d[i - 1] == "R" and d[i] == "R":
                beforeCount += 1
                continue
            beforeCount = 0
        return count

    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.max_score = 0
        self.res = [0] * len(aliceArrows)

        def cal(i: int, n: int, score: int, arr: List[int]):
            if i < 0 or n == 0:
                if score > self.max_score:
                    self.max_score = score
                    self.res = arr[:]
                    if n > 0:
                        self.res[0] += n
                return
            if aliceArrows[i] == 0:
                arr[i] = 1
                cal(i - 1, n - 1, score + i, arr)
                arr[i] = 0
            else:
                if aliceArrows[i] < n:
                    arr[i] = aliceArrows[i] + 1
                    cal(i - 1, n - aliceArrows[i] - 1, score + i, arr)
                    arr[i] = 0
                cal(i - 1, n, score, arr)
        cal(len(aliceArrows) - 1, numArrows, 0, [0] * len(aliceArrows))
        return self.res
