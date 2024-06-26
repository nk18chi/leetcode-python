from typing import Dict, List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        result: float = float("inf")
        left: int = 0
        right: int = len(nums) - 1
        while left < right:
            n: float = (nums[left] + nums[right]) / 2
            result = min(result, n)
            left += 1
            right -= 1
        return result

    def minimumArea(self, grid: List[List[int]]) -> int:
        rectangle: Dict[str, int] = {
            "top": len(grid),
            "bottom": 0,
            "left": len(grid[0]),
            "right": 0,
        }
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                rectangle["top"] = min(rectangle["top"], i + 1)
                rectangle["bottom"] = max(rectangle["bottom"], i + 1)
                rectangle["left"] = min(rectangle["left"], j + 1)
                rectangle["right"] = max(rectangle["right"], j + 1)
        return (rectangle["bottom"] - rectangle["top"] + 1) * (
            rectangle["right"] - rectangle["left"] + 1
        )

    def maximumTotalCost(self, nums):
        result: Dict[str, int] = {"add": nums[0], "sub": nums[0]}
        for i in range(1, len(nums)):
            current_add = result["add"]
            result["add"] = max(result["add"], result["sub"]) + nums[i]
            result["sub"] = current_add - nums[i]
        return max(result["add"], result["sub"])
