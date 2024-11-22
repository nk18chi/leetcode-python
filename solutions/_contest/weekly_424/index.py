from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total: int = sum(nums)
        cur: int = 0
        result: int = 0
        for n in nums:
            cur += n
            if n == 0:
                if cur == total - cur:
                    result += 2
                if abs(total - cur - cur) == 1:
                    result += 1
        return result

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff: List[int] = [0] * (len(nums) + 1)
        for query in queries:
            left, right = query
            diff[left] -= 1
            diff[right + 1] += 1
        cur: int = 0
        for i in range(len(diff) - 1):
            cur += diff[i]
            nums[i] += cur
        return all(x <= 0 for x in nums)

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def sweep_line(index: int) -> bool:
            diff: List[int] = [0] * (len(nums) + 1)
            for query in queries[:index]:
                left, right, value = query
                diff[left] -= value
                diff[right + 1] += value
            cur: int = 0
            array: List[int] = nums.copy()
            for i in range(len(diff) - 1):
                cur += diff[i]
                array[i] += cur
            return all(x <= 0 for x in array)

        if not sweep_line(len(queries)):
            return -1

        left: int = 0
        right: int = len(queries) - 1
        while left <= right:
            mid: int = (right + left) // 2
            res: bool = sweep_line(mid)
            if res:
                right = mid - 1
            else:
                left = mid + 1
        return left
